from django.core.management import call_command
from django.urls import reverse
from mapbox_baselayer.models import MapBaseLayer
from rest_framework import status
from rest_framework.test import APITestCase


class SettingsViewTestCase(APITestCase):
    def test_view(self):
        response = self.client.get(reverse('terra_settings:settings'))
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

    def test_create(self):
        pass

    def test_partial_update(self):
        pass

    def test_full_update(self):
        pass

    def test_delete(self):
        pass
