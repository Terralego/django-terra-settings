from mapbox_baselayer.models import MapBaseLayer, BaseLayerTile
from rest_framework import serializers


class BaseLayerTileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseLayerTile
        fields = ('url', )


class MapBaseLayerSerializer(serializers.ModelSerializer):
    tiles = BaseLayerTileSerializer(many=True)

    class Meta:
        model = MapBaseLayer
        fields = "__all__"
