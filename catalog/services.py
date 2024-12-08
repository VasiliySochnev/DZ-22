from .models import Product
from django.core.cache import cache


class ProductService:

    @classmethod
    def get_products(cls):
        return Product.objects.all()

    @classmethod
    def get_product_by_id(cls, product_id):
        return Product.objects.get(id=product_id)

    @classmethod
    def get_published_products(cls):
        return Product.objects.filter(unpublish_product=True)

    @classmethod
    def get_product_by_name(cls, name_product):
        return Product.objects.get(name=name_product)

    @classmethod
    def get_published_products_by_name(cls, name_product):
        return Product.objects.filter(name=name_product, unpublish_product=True)

    @classmethod
    def get_published_products_by_category(cls, category_id):
        cache_key = f"products_queryset{category_id}"
        products = cache.get(cache_key)

        if products is None:
            products = list(Product.objects.filter(category_id=category_id, unpublish_product=True))
            cache.set(cache_key, products, 60 * 1)

        return products

    @classmethod
    def get_published_products_by_category_name(cls, name_category):
        return Product.objects.filter(name_category=name_category, unpublish_product=True)

