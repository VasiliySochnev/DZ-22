from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig
from config import settings
from django.conf.urls.static import static

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.product_list, name='product_list'),
    path("product_info/<int:pk>/", views.product_info, name='product_info'),
    path("contacts/", views.contacts, name='contacts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)