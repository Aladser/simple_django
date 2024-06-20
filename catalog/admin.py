from django.contrib import admin

from catalog.models import Category, Product


# Register your models here.
@admin.register(Category)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    list_filter = ('is_active',)
    search_fields = ('name', 'description',)


@admin.register(Product)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'ava', 'price', 'is_active', 'category', 'created_at', 'updated_at')
    list_filter = ('is_active', 'category')
    search_fields = ('name', 'description', 'price')
