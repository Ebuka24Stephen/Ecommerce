from django.contrib import admin
from .models import Product, Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name', )}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'available',
        'price',
        'stock'
    ]

    prepopulated_fields = {'slug':('name', )}
