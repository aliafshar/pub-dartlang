import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

API_NAME = 'pub'
API_VERSION = 'v2'
API_DESCRIPTION = 'Pub, Dart package repository API.'


class PackageRequest(messages.Message):
  name = messages.StringField(1)

class PackageResponse(messages.Message):
  name = messages.StringField(1)

@endpoints.api(name=API_NAME, version=API_VERSION, description=API_DESCRIPTION)
class PubApi(remote.Service):
  """Endpoints service for the Pub API."""

  @endpoints.method(PackageRequest, PackageResponse, name='packages.get')
  def package_get(self, request):
    return PackageResponse(name=request.name + '!!!')

application = endpoints.api_server([PubApi])
