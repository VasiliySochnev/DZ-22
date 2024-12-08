from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, CategoryProductsListView
from config import settings
from django.conf.urls.static import static

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.ProductListView.as_view(), name="product_list"),
    path("product_detail/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("contacts/", views.ContactsTemplateView.as_view(), name="contacts"),
    path("product_form/", views.ProductCreateView.as_view(), name="product_create"),
    path("product_update/<int:pk>/", views.ProductUpdateView.as_view(), name="product_update"),
    path("product_confirm_delete/<int:pk>/", views.ProductDeleteView.as_view(), name="product_delete"),
    path("category_products_list/<int:category_id>", CategoryProductsListView.as_view(), name="category_products_list"),
    path("category_list", CategoryListView.as_view(), name="category_list"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
