from django.contrib import admin
from .models import Category, Product
from my_blog.models import My_blog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name_category",
    )
    list_filter = ("name_category",)
    search_fields = (
        "name_category",
        "descriptions_category",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name_product",
        "purchase_price",
        "category",
    )
    list_filter = ("category",)
    search_fields = (
        "name_product",
        "description_product",
    )


@admin.register(My_blog)
class My_blogAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "content",
        "preview",
    )
    list_filter = ("title",)
    search_fields = ("title",)
