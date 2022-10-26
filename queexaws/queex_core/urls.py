from email.mime import base
from django import views
from django.urls import path, include
from .views import ProductList, ProductDetail,ProductByCategory

urlpatterns = [
    path('', ProductList.as_view(), name='product-list'),
    path('product', ProductByCategory.as_view(), name='product-list'),
    path('product/<int:pk>', ProductDetail.as_view(), name='product_list')
]
