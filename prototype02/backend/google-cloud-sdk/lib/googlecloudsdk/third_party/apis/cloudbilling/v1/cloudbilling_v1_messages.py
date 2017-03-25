"""Generated message classes for cloudbilling version v1.

Allows developers to manage billing for their Google Cloud Platform projects
programmatically.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding


package = 'cloudbilling'


class BillingAccount(_messages.Message):
  """A billing account in [Google Cloud
  Console](https://console.cloud.google.com/). You can assign a billing
  account to one or more projects.

  Fields:
    displayName: The display name given to the billing account, such as `My
      Billing Account`. This name is displayed in the Google Cloud Console.
    name: The resource name of the billing account. The resource name has the
      form `billingAccounts/{billing_account_id}`. For example,
      `billingAccounts/012345-567890-ABCDEF` would be the resource name for
      billing account `012345-567890-ABCDEF`.
    open: True if the billing account is open, and will therefore be charged
      for any usage on associated projects. False if the billing account is
      closed, and therefore projects associated with it will be unable to use
      paid services.
  """

  displayName = _messages.StringField(1)
  name = _messages.StringField(2)
  open = _messages.BooleanField(3)


class CloudbillingBillingAccountsGetRequest(_messages.Message):
  """A CloudbillingBillingAccountsGetRequest object.

  Fields:
    name: The resource name of the billing account to retrieve. For example,
      `billingAccounts/012345-567890-ABCDEF`.
  """

  name = _messages.StringField(1, required=True)


class CloudbillingBillingAccountsListRequest(_messages.Message):
  """A CloudbillingBillingAccountsListRequest object.

  Fields:
    pageSize: Requested page size. The maximum page size is 100; this is also
      the default.
    pageToken: A token identifying a page of results to return. This should be
      a `next_page_token` value returned from a previous `ListBillingAccounts`
      call. If unspecified, the first page of results is returned.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)


class CloudbillingBillingAccountsProjectsListRequest(_messages.Message):
  """A CloudbillingBillingAccountsProjectsListRequest object.

  Fields:
    name: The resource name of the billing account associated with the
      projects that you want to list. For example,
      `billingAccounts/012345-567890-ABCDEF`.
    pageSize: Requested page size. The maximum page size is 100; this is also
      the default.
    pageToken: A token identifying a page of results to be returned. This
      should be a `next_page_token` value returned from a previous
      `ListProjectBillingInfo` call. If unspecified, the first page of results
      is returned.
  """

  name = _messages.StringField(1, required=True)
  pageSize = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(3)


class CloudbillingProjectsGetBillingInfoRequest(_messages.Message):
  """A CloudbillingProjectsGetBillingInfoRequest object.

  Fields:
    name: The resource name of the project for which billing information is
      retrieved. For example, `projects/tokyo-rain-123`.
  """

  name = _messages.StringField(1, required=True)


class CloudbillingProjectsUpdateBillingInfoRequest(_messages.Message):
  """A CloudbillingProjectsUpdateBillingInfoRequest object.

  Fields:
    name: The resource name of the project associated with the billing
      information that you want to update. For example, `projects/tokyo-
      rain-123`.
    projectBillingInfo: A ProjectBillingInfo resource to be passed as the
      request body.
  """

  name = _messages.StringField(1, required=True)
  projectBillingInfo = _messages.MessageField('ProjectBillingInfo', 2)


class ListBillingAccountsResponse(_messages.Message):
  """Response message for `ListBillingAccounts`.

  Fields:
    billingAccounts: A list of billing accounts.
    nextPageToken: A token to retrieve the next page of results. To retrieve
      the next page, call `ListBillingAccounts` again with the `page_token`
      field set to this value. This field is empty if there are no more
      results to retrieve.
  """

  billingAccounts = _messages.MessageField('BillingAccount', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListProjectBillingInfoResponse(_messages.Message):
  """Request message for `ListProjectBillingInfoResponse`.

  Fields:
    nextPageToken: A token to retrieve the next page of results. To retrieve
      the next page, call `ListProjectBillingInfo` again with the `page_token`
      field set to this value. This field is empty if there are no more
      results to retrieve.
    projectBillingInfo: A list of `ProjectBillingInfo` resources representing
      the projects associated with the billing account.
  """

  nextPageToken = _messages.StringField(1)
  projectBillingInfo = _messages.MessageField('ProjectBillingInfo', 2, repeated=True)


class ProjectBillingInfo(_messages.Message):
  """Encapsulation of billing information for a Cloud Console project. A
  project has at most one associated billing account at a time (but a billing
  account can be assigned to multiple projects).

  Fields:
    billingAccountName: The resource name of the billing account associated
      with the project, if any. For example,
      `billingAccounts/012345-567890-ABCDEF`.
    billingEnabled: True if the project is associated with an open billing
      account, to which usage on the project is charged. False if the project
      is associated with a closed billing account, or no billing account at
      all, and therefore cannot use paid services. This field is read-only.
    name: The resource name for the `ProjectBillingInfo`; has the form
      `projects/{project_id}/billingInfo`. For example, the resource name for
      the billing information for project `tokyo-rain-123` would be `projects
      /tokyo-rain-123/billingInfo`. This field is read-only.
    projectId: The ID of the project that this `ProjectBillingInfo`
      represents, such as `tokyo-rain-123`. This is a convenience field so
      that you don't need to parse the `name` field to obtain a project ID.
      This field is read-only.
  """

  billingAccountName = _messages.StringField(1)
  billingEnabled = _messages.BooleanField(2)
  name = _messages.StringField(3)
  projectId = _messages.StringField(4)


class StandardQueryParameters(_messages.Message):
  """Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    bearer_token: OAuth bearer token.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    pp: Pretty-print response.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    """Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    """V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  bearer_token = _messages.StringField(4)
  callback = _messages.StringField(5)
  fields = _messages.StringField(6)
  key = _messages.StringField(7)
  oauth_token = _messages.StringField(8)
  pp = _messages.BooleanField(9, default=True)
  prettyPrint = _messages.BooleanField(10, default=True)
  quotaUser = _messages.StringField(11)
  trace = _messages.StringField(12)
  uploadType = _messages.StringField(13)
  upload_protocol = _messages.StringField(14)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv',
    package=u'cloudbilling')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1',
    package=u'cloudbilling')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2',
    package=u'cloudbilling')
