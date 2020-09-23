from django.urls import path

from terra_settings.views import SettingsView, BaseLayerView

app_name = 'terra_settings'

urlpatterns = [
    path('settings/', SettingsView.as_view(), name='settings'),
    path('baselayer', BaseLayerView.as_view(), name='baselayer'),
]
