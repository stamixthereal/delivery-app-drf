from django.contrib import admin

from .models import Customer, OrderItem, Product, Restaurant


admin.site.register(Product)

admin.site.register(Restaurant)

admin.site.register(OrderItem)