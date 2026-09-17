from django.db import models
from django.core.exceptions import ValidationError

class StoreSettings(models.Model):
  store_name = models.CharField(max_length=150)
  email = models.EmailField(blank=True)
  phone = models.CharField(max_length=20, blank=True)
  currency = models.CharField(max_length=3, default="SAR")
  address = models.TextField(blank=True)
  description  = models.TextField(blank=True)
  tax_enabled = models.BooleanField(default=False)
  tax_percentage = models.DecimalField( max_digits=5 , decimal_places=2, default=0)
  delivery_enabled = models.BooleanField(default=True)
  minimum_order_amount = models.DecimalField( max_digits=10, decimal_places=2, default=0)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  whatsapp = models.CharField(max_length=20, blank=True)
  primary_color = models.CharField(max_length=7, blank=True)
  secondary_color = models.CharField(max_length=7, blank=True)    

  def save(self, *args, **kwargs):
    if not self.pk and StoreSettings.objects.exists():
      raise ValidationError("StoreSettings can only be created once.")

    super().save(*args, **kwargs)
