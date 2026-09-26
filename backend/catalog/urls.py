from django.urls import path
from .views import CategoryListView, ProductListView, ProductOneView

urlpatterns = [path("categories/", CategoryListView.as_view(), name="category-list")
              , path("products/", ProductListView.as_view(), name="products-list")
              , path("products/<slug:slug>/", ProductOneView.as_view(), name="product-detail")
               ]