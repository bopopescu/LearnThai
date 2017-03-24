# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Implements the command for modifying the user's SSH config."""
import cStringIO
import getpass
import os
import re
import stat
import textwrap

from googlecloudsdk.api_lib.compute import base_classes
from googlecloudsdk.api_lib.compute import lister
from googlecloudsdk.api_lib.compute import path_simplifier
from googlecloudsdk.calliope import exceptions
from googlecloudsdk.command_lib.compute import ssh_utils
from googlecloudsdk.command_lib.util import ssh
from googlecloudsdk.core import log
from googlecloudsdk.core import properties
from googlecloudsdk.core.util import files
from googlecloudsdk.core.util import platforms


# DO NOT CHANGE THE NEXT TWO LINES.
#
# Some clients depend on these two delimiters, so changing them will
# be very problematic for those clients.
_BEGIN_MARKER = '# Google Compute Engine Section'
_END_MARKER = '# End of Google Compute Engine Section'

# The "?" in the regex makes the regex non-greedy, so we don't
# accidentally wipe out data between two Compute sections.
_COMPUTE_SECTION_RE = '({begin_marker}.*?{end_marker}\n?)'.format(
    begin_marker=_BEGIN_MARKER, end_marker=_END_MARKER)

_HEADER = """\
The following has been auto-generated by "gcloud compute config-ssh"
to make accessing your Google Compute Engine virtual machines easier.

To remove this blob, run:

  gcloud compute config-ssh --remove

You can also manually remove this blob by deleting everything from
here until the comment that contains the string "End of Google Compute
Engine Section".

You should not hand-edit this section, unless you are deleting it.
"""


def _CreateAlias(instance_resource):
  """Returns the alias for the given instance."""
  parts = [
      instance_resource.name,
      path_simplifier.Name(instance_resource.zone),
      properties.VALUES.core.project.Get(required=True),
  ]
  return '.'.join(parts)


def _BuildComputeSection(instances, private_key_file, known_hosts_file):
  """Returns a string representing the Compute section that should be added."""
  buf = cStringIO.StringIO()
  buf.write(_BEGIN_MARKER)
  buf.write('\n')
  buf.write('#\n')

  for line in _HEADER.split('\n'):
    buf.write('#')
    if line:
      buf.write(' ')
      buf.write(line)
    buf.write('\n')

  for instance in instances:
    external_ip_address = (
        ssh_utils.GetExternalIPAddress(instance, no_raise=True))
    host_key_alias = 'compute.{0}'.format(instance.id)

    if external_ip_address:
      buf.write(textwrap.dedent("""\
          Host {alias}
              HostName {external_ip_address}
              IdentityFile {private_key_file}
              UserKnownHostsFile={known_hosts_file}
              HostKeyAlias={host_key_alias}
              IdentitiesOnly=yes
              CheckHostIP=no

          """.format(alias=_CreateAlias(instance),
                     external_ip_address=external_ip_address,
                     private_key_file=private_key_file,
                     known_hosts_file=known_hosts_file,
                     host_key_alias=host_key_alias)))

  buf.write(_END_MARKER)
  buf.write('\n')
  return buf.getvalue()


class ConfigSSH(ssh_utils.BaseSSHCommand):
  """Populate SSH config files with Host entries from each instance."""

  @staticmethod
  def Args(parser):
    ssh_utils.BaseSSHCommand.Args(parser)

    ssh_config_file = parser.add_argument(
        '--ssh-config-file',
        help='Specifies an alternative per-user SSH configuration file.')
    ssh_config_file.detailed_help = """\
        Specifies an alternative per-user SSH configuration file. By
        default, this is ``{0}''.
        """.format(ssh.PER_USER_SSH_CONFIG_FILE)

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help=('If provided, the proposed changes to the SSH config file are '
              'printed to standard output and no actual changes are made.'))

    parser.add_argument(
        '--remove',
        action='store_true',
        help=('If provided, any changes made to the SSH config file by this '
              'tool are reverted.'))

  def GetInstances(self):
    """Returns a generator of all instances in the project."""
    compute = self.compute
    errors = []
    instances = lister.GetZonalResources(
        service=compute.instances,
        project=self.project,
        requested_zones=None,
        filter_expr=None,
        http=self.http,
        batch_url=self.batch_url,
        errors=errors)

    if errors:
      base_classes.RaiseToolException(
          errors, error_message='Could not fetch all instances:')
    return instances

  def Run(self, args):
    super(ConfigSSH, self).Run(args)
    self.keys.EnsureKeysExist(args.force_key_file_overwrite)

    ssh_config_file = os.path.expanduser(
        args.ssh_config_file or ssh.PER_USER_SSH_CONFIG_FILE)

    instances = None
    if args.remove:
      compute_section = ''
    else:
      self.EnsureSSHKeyIsInProject(getpass.getuser())
      instances = list(self.GetInstances())
      if instances:
        compute_section = _BuildComputeSection(instances, self.keys.key_file,
                                               ssh.KnownHosts.DEFAULT_PATH)
      else:
        compute_section = ''

    try:
      existing_content = files.GetFileContents(ssh_config_file)
    except files.Error as e:
      existing_content = ''
      log.debug('SSH Config File [{0}] could not be opened: {1}'
                .format(ssh_config_file, e))
    if existing_content:
      section_re = re.compile(_COMPUTE_SECTION_RE,
                              flags=re.MULTILINE | re.DOTALL)
      match = section_re.search(existing_content)
      if not match:
        # There are no existing Compute Engine sections. If there is
        # at least one instance in the project (signified by
        # compute_section not being None), we append it to the end of
        # the configs. Otherwise, we set content to None which will
        # cause nothing to be written to the SSH config file.
        if compute_section:
          # Ensures that there is a blank line between the existing
          # configs and the Compute section.
          if existing_content[-1] != '\n':
            existing_content += '\n'
          if existing_content[-2:] != '\n\n':
            existing_content += '\n'
          new_content = existing_content + compute_section

        else:
          new_content = existing_content

      elif section_re.search(existing_content[match.end(1):]):
        # Multiple Compute Engine sections.
        raise exceptions.ToolException(
            'Found more than one Google Compute Engine section in [{0}]. '
            'You can either delete [{0}] and let this command recreate it for '
            'you or you can manually delete all sections marked with '
            '[{1}] and [{2}].'
            .format(ssh_config_file, _BEGIN_MARKER, _END_MARKER))
      else:
        # One Compute Engine section -- replace it.
        new_content = '{before}{new}{after}'.format(
            before=existing_content[0:match.start(1)],
            new=compute_section,
            after=existing_content[match.end(1):])

    else:
      new_content = compute_section

    if args.dry_run:
      log.out.write(new_content or '')
      return

    if new_content != existing_content:
      if (os.path.exists(ssh_config_file) and
          platforms.OperatingSystem.Current() is not
          platforms.OperatingSystem.WINDOWS):
        ssh_config_perms = os.stat(ssh_config_file).st_mode
        # From `man 5 ssh_config`:
        #    this file must have strict permissions: read/write for the user,
        #    and not accessible by others.
        # We check that here:
        if not (
            ssh_config_perms & stat.S_IRWXU == stat.S_IWUSR | stat.S_IRUSR and
            ssh_config_perms & stat.S_IWGRP == 0 and
            ssh_config_perms & stat.S_IWOTH == 0):
          log.warn('Invalid permissions on [{0}]. Please change to match ssh '
                   'requirements (see man 5 ssh).')
      # TODO(user): This write will not work very well if there is
      # a lot of write contention for the SSH config file. We should
      # add a function to do a better job at "atomic file writes".
      with files.OpenForWritingPrivate(ssh_config_file) as f:
        f.write(new_content)

    if compute_section:
      log.out.write(textwrap.dedent("""\
          You should now be able to use ssh/scp with your instances.
          For example, try running:

            $ ssh {alias}

          """.format(alias=_CreateAlias(instances[0]))))

    elif not instances and not args.remove:
      log.warn(
          'No host aliases were added to your SSH configs because you do not '
          'have any instances. Try running this command again after creating '
          'some instances.')


ConfigSSH.detailed_help = {
    'brief': 'Populate SSH config files with Host entries from each instance',
    'DESCRIPTION': """\
        *{command}* makes SSHing to virtual machine instances easier
        by adding an alias for each instance to the user SSH configuration
        (``~/.ssh/config'') file.

        In most cases, it is sufficient to run:

          $ {command}

        Each instance will be given an alias of the form
        ``NAME.ZONE.PROJECT''. For example, if ``example-instance'' resides in
        ``us-central1-a'', you can SSH to it by running:

          $ ssh example-instance.us-central1-a.MY-PROJECT

        On some platforms, the host alias can be tab-completed, making
        the long alias less daunting to type.

        The aliases created interface with SSH-based programs like
        *scp(1)*, so it is possible to use the aliases elsewhere:

          $ scp ~/MY-FILE example-instance.us-central1-a.MY-PROJECT:~

        Whenever instances are added, removed, or their external IP
        addresses are changed, this command should be re-executed to
        update the configuration.

        This command ensures that the user's public SSH key is present
        in the project's metadata. If the user does not have a public
        SSH key, one is generated using *ssh-keygen(1)* (if the `--quiet`
        flag is given, the generated key will have an empty passphrase).
        """
}
