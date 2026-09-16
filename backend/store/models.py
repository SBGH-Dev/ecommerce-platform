from django.db import models

class StoreSettings(models.Model):
  store_name = models.CharField(max_length=150)
  email = models.EmailField(blank=True)
  phone = models.CharField(max_length=20, blank=True)
  currency = models.CharField(max_length=3, default="SAR")
  address = models.TextField(blank=True)
