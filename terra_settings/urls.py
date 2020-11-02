from django.urls import path, include
from rest_framework.routers import SimpleRouter
from terra_settings.views import SettingsView
from terra_settings.base_layers.views import BaseLayerViewSet

router = SimpleRouter()
router.register('baselayer', BaseLayerViewSet, basename='baselayer')

urlpatterns = [
    path('settings/', SettingsView.as_view(), name='settings'),
    path('', include(router.urls)),
]
