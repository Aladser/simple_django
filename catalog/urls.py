from django.contrib import admin
from django.urls import path

from catalog.views import product
from catalog.views.views import contacts

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', product.index),
    path('product/<int:pk>', product.show),
    path('product/create/', product.create),
    path('product/', product.store),

    path('contacts/', contacts),
]
