from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.home, name='contacts'),
    path("contacts/", views.home, name='home'),
]