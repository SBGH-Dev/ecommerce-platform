from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    def create_user(self, email, password=None, **extra_fields):
      email = self.normalize_email(email)
      user = self.model(email=email, **extra_fields)
      user.set_password(password)
      user.save()
      return user

    def create_superuser (self, email, password=None, **extra_fields):
      extra_fields.setdefault("is_staff", True)
      extra_fields.setdefault("is_superuser", True)
      return self.create_user(email, password, **extra_fields)

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
  objects = CustomUserManager()