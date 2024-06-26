from django.contrib import admin
from django.urls import path
from catalog.views import index, contacts, product_show

urlpatterns = [
    path('', index),
    path('products/<int:pk>', product_show),
    path('contacts/', contacts),
    path('admin/', admin.site.urls)
]
