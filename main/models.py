from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
from django_countries.fields import CountryField


class Customer(models.Model):
    """Customer model"""

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100, blank=True, )
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(unique=True)

    def __str__(self):
        return f'Customer: {self.first_name} {self.last_name}'


class Adress(models.Model):
    """Adress model"""

    country = CountryField()
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=150)
    house = models.IntegerField()

    def __str__(self):
        return f'{self.country} {self.city}'


class MenuItem(models.Model):
    """Menu model"""

    name = models.CharField(max_length=150)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} from {self.restaurant} for {self.price}$'


class Restaurant(models.Model):
    """Restaurant model"""

    name = models.CharField(max_length=150)


class OrderItem(models.Model):
    """Dish per order"""

    item = models.ForeignKey('MenuItem', on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.item.name}'

    def price(self):
        return self.item.price


class Order(models.Model):
    """Order model"""

    date = models.DateField(default=datetime.now)
    customer = models.ForeignKey('Customer', on_delete=models.PROTECT)
    adress = models.OneToOneField('Adress', on_delete=models.CASCADE)
    items = models.ManyToManyField('OrderItem')
    restaurant = models.ForeignKey('Restaurant', on_delete=models.PROTECT)
    sum_price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    is_shipped = models.BooleanField(default=False)

    def __str__(self):
        return f'Order: {self.items} from {self.restaurant}'

    def final_price(self):
        return self.items.price() * self.items.quantity