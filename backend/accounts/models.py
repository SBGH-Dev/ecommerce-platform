from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    def create_user(self, email, password=None, **kwargs):
      if not email:
        raise ValueError("Email Is Required")
      
      email = self.normalize_email(email)
      user = self.model(email=email, **kwargs)
      user.set_password(password)
      user.save()
      return user

    def create_superuser (self, email, password=None, **kwargs):
      kwargs.setdefault("is_staff", True)
      kwargs.setdefault("is_superuser", True)

      if kwargs.get("is_staff") is not True:
        raise ValueError("is_staff must be ture")
            
      if kwargs.get("is_superuser") is not True:
        raise ValueError("is_superuser must be ture")
      
      return self.create_user(email, password, **kwargs)

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