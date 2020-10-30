from mapbox_baselayer.models import MapBaseLayer, BaseLayerTile
from rest_framework import serializers


class BaseLayerTileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseLayerTile
        fields = ('url', )

    def to_representation(self, instance):
        return instance.url

    def to_internal_value(self, data):
        return data


class MapBaseLayerSerializer(serializers.ModelSerializer):
    tiles = BaseLayerTileSerializer(many=True)

    class Meta:
        model = MapBaseLayer
        fields = "__all__"

    def create(self, validated_data):
        """ handle sub tile definition """
        tiles = validated_data.pop('tiles')
        instance = MapBaseLayer.objects.create(**validated_data)
        for tile in tiles:
            BaseLayerTile.objects.create(base_layer=instance, url=tile)
        return instance

    def update(self, instance, validated_data):
        """ handle sub tile definition """
        tiles = validated_data.pop('tiles')
        for key, value in validated_data.items():
            # update data for each instance validated value
            setattr(instance, key, value)
        # delete tiles not in putted data
        instance.tiles.exclude(url__in=[tile for tile in tiles]).delete()
        tile_instances = [
            BaseLayerTile.objects.get_or_create(url=tile,
                                                base_layer=instance)[0] for tile in tiles
        ]
        instance.tiles.set(tile_instances)
        instance.save()
        return instance
