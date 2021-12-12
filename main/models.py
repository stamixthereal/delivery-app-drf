from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    """Customer's model"""

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(unique=True)