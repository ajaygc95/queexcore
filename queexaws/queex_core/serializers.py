from .models import Product, Category
from rest_framework import serializers



class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields="__all__"

class ProductSerializers(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field="name"
    )
    class Meta:
        model = Product
        fields =['upc','name','description','category','quantity','price','cost']