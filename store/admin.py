from django.contrib import admin
from django.db.models import Count

from . import models


# Register your models here.
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'inventory_status',
                    'collection_title']
    list_editable = ['price']
    list_per_page = 10
    list_select_related = ['collection']

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return "LOW"
        return "OK"


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_editable = ['membership']
    list_display = ['first_name', 'last_name', 'membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer']
    list_per_page = 10
    ordering = ['placed_at']


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        return collection.products_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )
