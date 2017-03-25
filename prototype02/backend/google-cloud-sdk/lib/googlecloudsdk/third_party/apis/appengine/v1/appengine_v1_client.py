"""Generated client library for appengine version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.appengine.v1 import appengine_v1_messages as messages


class AppengineV1(base_api.BaseApiClient):
  """Generated client library for service appengine version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://appengine.googleapis.com/'

  _PACKAGE = u'appengine'
  _SCOPES = [u'https://www.googleapis.com/auth/appengine.admin', u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/cloud-platform.read-only']
  _VERSION = u'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'AppengineV1'
  _URL_VERSION = u'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new appengine handle."""
    url = url or self.BASE_URL
    super(AppengineV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.apps_locations = self.AppsLocationsService(self)
    self.apps_operations = self.AppsOperationsService(self)
    self.apps_services_versions_instances = self.AppsServicesVersionsInstancesService(self)
    self.apps_services_versions = self.AppsServicesVersionsService(self)
    self.apps_services = self.AppsServicesService(self)
    self.apps = self.AppsService(self)

  class AppsLocationsService(base_api.BaseApiService):
    """Service class for the apps_locations resource."""

    _NAME = u'apps_locations'

    def __init__(self, client):
      super(AppengineV1.AppsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      """Get information about a location.

      Args:
        request: (AppengineAppsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/apps/{appsId}/locations/{locationsId}',
        http_method=u'GET',
        method_id=u'appengine.apps.locations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'AppengineAppsLocationsGetRequest',
        response_type_name=u'Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists information about the supported locations for this service.

      Args:
        request: (AppengineAppsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/apps/{appsId}/locations',
        http_method=u'GET',
        method_id=u'appengine.apps.locations.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1/{+name}/locations',
        request_field='',
        request_type_name=u'AppengineAppsLocationsListRequest',
        response_type_name=u'ListLocationsResponse',
        supports_download=False,
    )

  class AppsOperationsService(base_api.BaseApiService):
    """Service class for the apps_operations resource."""

    _NAME = u'apps_operations'

    def __init__(self, client):
      super(AppengineV1.AppsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      """Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (AppengineAppsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/apps/{appsId}/operations/{operationsId}',
        http_method=u'GET',
        method_id=u'appengine.apps.operations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'AppengineAppsOperationsGetRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns UNIMPLEMENTED.NOTE: the name binding below allows API services to override the binding to use different resource name schemes, such as users/*/operations.

      Args:
        request: (AppengineAppsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/apps/{appsId}/operations',
        http_method=u'GET',
        method_id=u'appengine.apps.operations.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1/{+name}/operations',
        request_field='',
        request_type_name=u'AppengineAppsOperationsListRequest',
        response_type_name=u'ListOperationsResponse',
        supports_download=False,
    )

  class AppsServicesVersionsInstancesService(base_api.BaseApiService):
    """Service class for the apps_services_versions_instances resource."""

    _NAME = u'apps_services_versions_instances'

    def __init__(self, client):
      super(AppengineV1.AppsServicesVersionsInstancesService, self).__init__(client)
      self._upload_configs = {
          }

    def Debug(self, request, global_params=None):
      """Enables debugging on a VM instance. This allows you to use the SSH command to connect to the virtual machine where the instance lives. While in "debug mode", the instance continues to serve live traffic. You should delete the instance when you are done debugging and then allow the system to take over and determine if another instance should be started.Only applicable for instances in App Engine flexible environment.

      Args:
        request: (AppengineAppsServicesVersionsInstancesDebugRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Debug')
      return self._RunMethod(
          config, request, global_params=global_params)

    Debug.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/apps/{appsId}/services/{servicesId}/versions/{versionsId}/instances/{instancesId}:debug',
        http_method=u'POST',
        method_id=u'appengine.apps.services.versions.instances.debug',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}:debug',
        request_field=u'debugInstanceRequest',
        request_type_name=u'AppengineAppsServicesVersionsInstancesDebugRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Stops a running instance.

      Args:
        request: (AppengineAppsServicesVersionsInstancesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/apps/{appsId}/services/{servicesId}/versions/{versionsId}/instances/{instancesId}',
        http_method=u'DELETE',
        method_id=u'appengine.apps.services.versions.instances.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'AppengineAppsServicesVersionsInstancesDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets instance information.

      Args:
        request: (AppengineAppsServicesVersionsInstancesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Instance) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/apps/{appsId}/services/{servicesId}/versions/{versionsId}/instances/{instancesId}',
        http_method=u'GET',
        method_id=u'appengine.apps.services.versions.instances.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'AppengineAppsServicesVersionsInstancesGetRequest',
        response_type_name=u'Instance',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists the instances of a version.

      Args:
        request: (AppengineAppsServicesVersionsInstancesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListInstancesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/apps/{appsId}/services/{servicesId}/versions/{versionsId}/instances',
        http_method=u'GET',
        method_id=u'appengine.apps.services.versions.instances.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1/{+parent}/instances',
        request_field='',
        request_type_name=u'AppengineAppsServicesVersionsInstancesListRequest',
        response_type_name=u'ListInstancesResponse',
        supports_download=False,
    )

  class AppsServicesVersionsService(base_api.BaseApiService):
    """Service class for the apps_services_versions resource."""

    _NAME = u'apps_services_versions'

    def __init__(self, client):
      super(AppengineV1.AppsServicesVersionsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Deploys code and resource files to a new version.

      Args:
        request: (AppengineAppsServicesVersionsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/apps/{appsId}/services/{servicesId}/versions',
        http_method=u'POST',
        method_id=u'appengine.apps.services.versions.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1/{+parent}/versions',
        request_field=u'version',
        request_type_name=u'AppengineAppsServicesVersionsCreateRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes an existing Version resource.

      Args:
        request: (AppengineAppsServicesVersionsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/apps/{appsId}/services/{servicesId}/versions/{versionsId}',
        http_method=u'DELETE',
        method_id=u'appengine.apps.services.versions.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'AppengineAppsServicesVersionsDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets the specified Version resource. By default, only a BASIC_VIEW will be returned. Specify the FULL_VIEW parameter to get the full resource.

      Args:
        request: (AppengineAppsServicesVersionsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Version) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/apps/{appsId}/services/{servicesId}/versions/{versionsId}',
        http_method=u'GET',
        method_id=u'appengine.apps.services.versions.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'view'],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'AppengineAppsServicesVersionsGetRequest',
        response_type_name=u'Version',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists the versions of a service.

      Args:
        request: (AppengineAppsServicesVersionsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListVersionsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/apps/{appsId}/services/{servicesId}/versions',
        http_method=u'GET',
        method_id=u'appengine.apps.services.versions.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken', u'view'],
        relative_path=u'v1/{+parent}/versions',
        request_field='',
        request_type_name=u'AppengineAppsServicesVersionsListRequest',
        response_type_name=u'ListVersionsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      """Updates the specified Version resource. You can specify the following fields depending on the App Engine environment and type of scaling that the version resource uses:.
serving_status (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.serving_status):  For Version resources that use basic scaling, manual scaling, or run in  the App Engine flexible environment.
instance_class (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.instance_class):  For Version resources that run in the App Engine standard environment.
automatic_scaling.min_idle_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling):  For Version resources that use automatic scaling and run in the App  Engine standard environment.
automatic_scaling.max_idle_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling):  For Version resources that use automatic scaling and run in the App  Engine standard environment.

      Args:
        request: (AppengineAppsServicesVersionsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/apps/{appsId}/services/{servicesId}/versions/{versionsId}',
        http_method=u'PATCH',
        method_id=u'appengine.apps.services.versions.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1/{+name}',
        request_field=u'version',
        request_type_name=u'AppengineAppsServicesVersionsPatchRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class AppsServicesService(base_api.BaseApiService):
    """Service class for the apps_services resource."""

    _NAME = u'apps_services'

    def __init__(self, client):
      super(AppengineV1.AppsServicesService, self).__init__(client)
      self._upload_configs = {
          }

    def Delete(self, request, global_params=None):
      """Deletes the specified service and all enclosed versions.

      Args:
        request: (AppengineAppsServicesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/apps/{appsId}/services/{servicesId}',
        http_method=u'DELETE',
        method_id=u'appengine.apps.services.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'AppengineAppsServicesDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets the current configuration of the specified service.

      Args:
        request: (AppengineAppsServicesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Service) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/apps/{appsId}/services/{servicesId}',
        http_method=u'GET',
        method_id=u'appengine.apps.services.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'AppengineAppsServicesGetRequest',
        response_type_name=u'Service',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists all the services in the application.

      Args:
        request: (AppengineAppsServicesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListServicesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/apps/{appsId}/services',
        http_method=u'GET',
        method_id=u'appengine.apps.services.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1/{+parent}/services',
        request_field='',
        request_type_name=u'AppengineAppsServicesListRequest',
        response_type_name=u'ListServicesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      """Updates the configuration of the specified service.

      Args:
        request: (AppengineAppsServicesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/apps/{appsId}/services/{servicesId}',
        http_method=u'PATCH',
        method_id=u'appengine.apps.services.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'migrateTraffic', u'updateMask'],
        relative_path=u'v1/{+name}',
        request_field=u'service',
        request_type_name=u'AppengineAppsServicesPatchRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class AppsService(base_api.BaseApiService):
    """Service class for the apps resource."""

    _NAME = u'apps'

    def __init__(self, client):
      super(AppengineV1.AppsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates an App Engine application for a Google Cloud Platform project. Required fields:.
id - The ID of the target Cloud Platform project.
location - The region (https://cloud.google.com/appengine/docs/locations) where you want the App Engine application located.For more information about App Engine applications, see Managing Projects, Applications, and Billing (https://cloud.google.com/appengine/docs/python/console/).

      Args:
        request: (Application) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'appengine.apps.create',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path=u'v1/apps',
        request_field='<request>',
        request_type_name=u'Application',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets information about an application.

      Args:
        request: (AppengineAppsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Application) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/apps/{appsId}',
        http_method=u'GET',
        method_id=u'appengine.apps.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'AppengineAppsGetRequest',
        response_type_name=u'Application',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      """Updates the specified Application resource. You can update the following fields:.
auth_domain - Google authentication domain for controlling user access to the application.
default_cookie_expiration - Cookie expiration policy for the application.

      Args:
        request: (AppengineAppsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/apps/{appsId}',
        http_method=u'PATCH',
        method_id=u'appengine.apps.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1/{+name}',
        request_field=u'application',
        request_type_name=u'AppengineAppsPatchRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Repair(self, request, global_params=None):
      """Recreates the required App Engine features for the specified App Engine application, for example a Cloud Storage bucket or App Engine service account. Use this method if you receive an error message about a missing feature, for example, Error retrieving the App Engine service account.

      Args:
        request: (AppengineAppsRepairRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Repair')
      return self._RunMethod(
          config, request, global_params=global_params)

    Repair.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/apps/{appsId}:repair',
        http_method=u'POST',
        method_id=u'appengine.apps.repair',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}:repair',
        request_field=u'repairApplicationRequest',
        request_type_name=u'AppengineAppsRepairRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )
