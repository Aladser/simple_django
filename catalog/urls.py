from django.contrib import admin
from django.urls import path

from catalog.views.product.views import index, show, create, store
from catalog.views.views import contacts

urlpatterns = [
    path('', index),
    path('product/<int:pk>', show),
    path('product/create/', create),
    path('product/', store),

    path('contacts/', contacts),
    path('admin/', admin.site.urls)
]
