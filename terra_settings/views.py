from django.conf import settings
from mapbox_baselayer.models import MapBaseLayer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from terra_settings.base_layers.serializers import MapBaseLayerSerializer
from terra_settings.settings import TERRA_APPLIANCE_SETTINGS


class SettingsView(APIView):
    """ This is public endpoint used to init terralego apps """
    permission_classes = (AllowAny, )

    def get(self, request):
        terra_settings = {
            # for the moment, language is fixed and defined by backend instance
            'language': settings.LANGUAGE_CODE.lower(),
            'base_layers': MapBaseLayerSerializer(MapBaseLayer.objects.all(), many=True).data,
        }

        terra_settings.update(TERRA_APPLIANCE_SETTINGS)

        return Response(terra_settings)
