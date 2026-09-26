from django.shortcuts import render
from rest_framework import generics
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryListView (generics.ListAPIView):
  queryset = Category.objects.filter(is_active = True)
  serializer_class = CategorySerializer

class ProductListView (generics.ListAPIView):
  queryset = Product.objects.filter(is_active=True)
  serializer_class = ProductSerializer

class ProductOneView (generics.RetrieveAPIView):
  queryset = Product.objects.filter(is_active = True)
  lookup_field = "slug"
  serializer_class = ProductSerializer