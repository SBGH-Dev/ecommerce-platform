from django.db import models

class Category (models.Model):
  name = models.CharField(max_length=150)
  slug = models.SlugField(max_length=150, unique=True)
  description = models.TextField(blank=True)
  is_active = models.BooleanField(default=True)
  sort_order = models.PositiveIntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="products")
    description = models.TextField(blank=True)
    base_price = models.DecimalField( max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.name