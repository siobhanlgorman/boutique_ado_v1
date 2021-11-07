from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """ fields to display """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        )


class CategoryAdmin(admin.ModelAdmin):
    """ fields to display """
    list_display = (
        'friendly_name',
        'name',
    )

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
