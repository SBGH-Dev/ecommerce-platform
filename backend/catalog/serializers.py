from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
  class Meta: 
    model = Category
    fields = [ "id",
            "name",
            "slug",
            "description",
            "is_active",
            "sort_order",]

class ProductSerializer(serializers.ModelSerializer):
  category_name = serializers.CharField(source = 'category.name', read_only = True)
  class Meta:
    model = Product
    fields =[
        "id",
        "name",
        "slug",
        "category_name",
        "category",
        "description",
        "base_price",
        "sku",
        "is_active",
        "is_featured",
        ]