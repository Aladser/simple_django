from django.contrib import admin
from django.urls import path
from catalog.views import index, contacts, product_show, product_create, product_store

urlpatterns = [
    path('', index),
    path('product/<int:pk>', product_show),
    path('product/create/', product_create),
    path('product/', product_store),

    path('contacts/', contacts),
    path('admin/', admin.site.urls)
]
