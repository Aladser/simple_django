from django.contrib import admin
from django.urls import path
from catalog.views import index, contacts, product_show, product_create

urlpatterns = [
    path('', index),
    path('product/<int:pk>', product_show),
    path('product/create/', product_create),
    path('contacts/', contacts),
    path('admin/', admin.site.urls)
]
