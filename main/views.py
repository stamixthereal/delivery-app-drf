from rest_framework import mixins, status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Product, Restaurant

from .serializers import (LoginSerializer, ProductListSerializer,
                          RegistrationSerializer, RestaurantListSerializer)


class RegistrationAPIView(APIView):
    """
    Registers a new user.
    """
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request):
        """
        Creates a new User object.
        Username, email, and password are required.
        Returns a JSON web token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                'token': serializer.data.get('token', None),
            },
            status=status.HTTP_201_CREATED,
        )


class LoginAPIView(APIView):
    """
    Logs in an existing user.
    """
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        """
        Checks is user exists.
        Email and password are required.
        Returns a JSON web token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductView(
            mixins.ListModelMixin,
            viewsets.GenericViewSet
            ):

    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]
    queryset = Product.objects.all()


class RestaurantView(
            mixins.ListModelMixin,
            viewsets.GenericViewSet
            ):

    serializer_class = RestaurantListSerializer
    permission_classes = [AllowAny]
    queryset = Restaurant.objects.all()