from django.core.management import call_command
from django.urls import reverse
from mapbox_baselayer.models import MapBaseLayer
from rest_framework import status
from rest_framework.test import APITestCase


class SettingsViewTestCase(APITestCase):
    def test_view(self):
        response = self.client.get(reverse('settings'))
        self.assertEqual(200, response.status_code)
        self.assertListEqual(
            ['jwt_delta', 'base_layers'],
            list(response.json())
        )


class MapBaseLayerViewsSetTesCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        call_command('install_osm_baselayer')

    def test_list(self):
        response = self.client.get(reverse('baselayer-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(len(data['results']) == 1)
        self.assertEqual(data['results'][0]['name'], 'OSM')

    def test_detail(self):
        pk = MapBaseLayer.objects.get().pk
        response = self.client.get(reverse('baselayer-detail', args=(pk, )))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data['name'], 'OSM')

    def test_tilejson_url_in_list(self):
        response = self.client.get(reverse('baselayer-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(len(data['results']) == 1)
        self.assertEqual(data['results'][0]['tilejson_url'], 'http://testserver/baselayer/1/tilejson/')

    def test_tilejson_in_list(self):
        pk = MapBaseLayer.objects.get().pk
        response = self.client.get(reverse('baselayer-detail', args=(pk, )))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        tilejson_url = data['tilejson_url']
        response = self.client.get(tilejson_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.json())

    def test_create(self):
        data = {
            "tiles": [
                "//test.org",
            ],
            "name": "test",
            "order": 0,
            "base_layer_type": "raster",
            "min_zoom": 0,
            "max_zoom": 20,
            "tile_size": 256
        }
        response = self.client.post(reverse('baselayer-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = response.json()
        self.assertTrue(data['id'])
        self.assertEqual(data['tiles'][0], "//test.org")

    def test_partial_update(self):
        data = {
            "tiles": [
                "//test2.org",
            ],
        }
        pk = MapBaseLayer.objects.get().pk
        response = self.client.patch(reverse('baselayer-detail', args=(pk, )), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data['tiles'][0], "//test2.org")

    def test_full_update(self):
        data = {
            "tiles": [
                "//test3.org",
            ],
            "name": "test",
            "order": 0,
            "base_layer_type": "raster",
            "min_zoom": 0,
            "max_zoom": 20,
            "tile_size": 256
        }
        pk = MapBaseLayer.objects.get().pk
        response = self.client.patch(reverse('baselayer-detail', args=(pk, )), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data['tiles'][0], "//test3.org")

    def test_delete(self):
        pk = MapBaseLayer.objects.get().pk
        response = self.client.delete(reverse('baselayer-detail', args=(pk, )))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
