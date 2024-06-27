from django.contrib import admin

from catalog.models import Category, Product, Contact


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'description',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category', 'is_active')
    list_filter = ('is_active', 'category')
    search_fields = ('name', 'description')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'number', 'address')
    list_filter = ('name', 'address')
    search_fields = ('name', 'number')
