from datetime import datetime, timedelta

import jwt
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from .manager import CustomUserManager


class Customer(AbstractUser):
    """
    Custom model of customer without username.
    Email as the main field.
    """
    username = None
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    @property
    def token(self):
        """
        Позволяет нам получить токен пользователя, вызвав
        user.token вместо user.generate_jwt_token().
        Декоратор @property выше делает это возможным.
        token называется «динамическим свойством».
        """
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        """
        Создает веб-токен JSON, в котором хранится идентификатор
        этого пользователя и срок его действия
        составляет 60 дней в будущем.
        """
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

    def __str__(self):
        return self.email


class Adress(models.Model):
    """
    Adress model
    """
    country = CountryField()
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=150)
    house = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Adress'
        verbose_name_plural = 'Adresses'

    def __str__(self):
        return f'{self.country} {self.city}'


class Product(models.Model):
    """
    Product model
    """
    name = models.CharField(max_length=150)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.name} from {self.restaurant} for {self.price}$'


class Restaurant(models.Model):
    """
    Restaurant model
    """
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'

    def __str__(self):
        return f'{self.name}'


class OrderItem(models.Model):
    """
    Dish per order
    """
    item = models.ForeignKey('Product', on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} {self.item.name}'


class Order(models.Model):
    """
    Order model
    """
    date = models.DateField(default=datetime.now)
    customer = models.ForeignKey('Customer', on_delete=models.PROTECT)
    adress = models.OneToOneField('Adress', on_delete=models.CASCADE)
    items = models.ManyToManyField('Cart')
    restaurant = models.ForeignKey('Restaurant', on_delete=models.PROTECT)
    sum_price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    is_shipped = models.BooleanField(default=False)
    phone = PhoneNumberField()

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'Order: {self.items} from {self.restaurant}'


class Cart(models.Model):
    """
    Cart for each user model
    """
    cart_id = models.OneToOneField('Customer', on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField('OrderItem')

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
        ordering = ['cart_id', '-created_at']

    def __str__(self):
        return f'{self.cart_id}'
