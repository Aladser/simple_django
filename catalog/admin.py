from django.contrib import admin

from catalog.models import Category, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_filter = ('is_active',)
    search_fields = ('name', 'description',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category')
    list_filter = ('is_active', 'category')
    search_fields = ('name', 'description')
