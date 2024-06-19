from django.contrib import admin

from catalog.models import Student


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname',)
    list_filter = ('is_active',)
    search_fields = ('name', 'surname',)