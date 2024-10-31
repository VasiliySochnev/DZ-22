from django.contrib import admin
from . models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_category',)
    list_filter = ('name_category',)
    search_fields = ('name_category', 'descriptions_category',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_product', 'purchase_price', 'category',)
    list_filter = ('category',)
    search_fields = ('name_product', 'description_product',)