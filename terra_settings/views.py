from django.conf import settings
from mapbox_baselayer.models import MapBaseLayer
from rest_framework.response import Response
from rest_framework.views import APIView

from terra_settings.settings import TERRA_APPLIANCE_SETTINGS


class SettingsView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def get(self, request):
        terra_settings = {
            # TODO: move this after terracommon.accounts split
            'jwt_delta': settings.JWT_AUTH['JWT_EXPIRATION_DELTA']
        }

        terra_settings.update(TERRA_APPLIANCE_SETTINGS)

        return Response(terra_settings)


class BaseLayerView(APIView):
    def get(self, request, *args, **kwargs):
        baselayers = [
            {
                "id": baselayer.id,
                "name": baselayer.name,
            }
            for baselayer in MapBaseLayer.objects.all()
        ]
        return Response(baselayers)
