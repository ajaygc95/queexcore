from requests import Response
from .models import Category, Product
from .serializers import CategorySerializers, ProductSerializers
from rest_framework import generics
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.views import APIView

class ProductList(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializers

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()


class ProductByCategory(generics.ListAPIView):
    serializer_class = ProductSerializers
    
    def get_queryset(self):
            queryset = Product.objects.all()
            search = self.request.query_params.get('category_name', None)
            if search:
                queryset = queryset.filter(category__name__icontains=search)
            return queryset