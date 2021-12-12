from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
from django_countries.fields import CountryField


class Customer(models.Model):
    """Customer model"""

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(unique=True)


class Adress(models.Model):
    """Adress model"""

    country = CountryField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=150, blank=True)
    house = models.IntegerField(blank=True)


class OrderDish(models.Model):
    """Dish per order"""

    dish_name = ''
    quantity = ''
    price = ''

class Order(models.Model):
    """Order model"""

    date = models.DateField(default=datetime.now, blank=True)
    customer = models.ForeignKey(Customer)
    adress = models.ForeignKey(Adress, on_delete=models.CASCADE)
    dishes = models.ForeignKey(OrderDish, on_delete=models.CASCADE)