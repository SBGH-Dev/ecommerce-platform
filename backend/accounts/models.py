from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  phone = models.CharField(max_length=20, blank=True)
  is_email_verified = models.BooleanField(default=False)
  class Role (models.TextChoices):
    CUSTOMER = "CUSTOMER", "Customer"
    OWNER = "OWNER", "Owner"
    ADMIN = "ADMIN", "Admin"
    STAFF = "STAFF", "Staff"
  role = models.CharField(max_length=20, choices=Role.choices,default=Role.CUSTOMER,)
  username = None
  email = models.EmailField(unique=True)
  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = []