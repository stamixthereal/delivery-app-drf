from rest_framework import serializers

from .models import Product, Restaurant, OrderItem


class ProductListSerializer(serializers.ModelSerializer):
    restaurant = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Product
        fields = ['name', 'price', 'restaurant']


class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name']


class ProductOrderingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'