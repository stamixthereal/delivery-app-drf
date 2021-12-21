from rest_framework import mixins, viewsets

from main.models import Product, Restaurant, OrderItem

from .serializers import ProductListSerializer, RestaurantListSerializer, ProductOrderingSerializer


class ProductView(
            mixins.ListModelMixin,
            mixins.RetrieveModelMixin,
            viewsets.GenericViewSet
            ):

    serializer_class = ProductListSerializer
    queryset = Product.objects.all()


class RestaurantView(
            mixins.ListModelMixin,
            mixins.RetrieveModelMixin,
            viewsets.GenericViewSet
            ):

    serializer_class = RestaurantListSerializer
    queryset = Restaurant.objects.all()


class ProductOrderView(
            mixins.CreateModelMixin,
            viewsets.GenericViewSet
            ):

    serializer_class = ProductOrderingSerializer
    queryset = OrderItem.objects.all()
