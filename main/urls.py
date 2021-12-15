from django.urls import re_path
from rest_framework.routers import DefaultRouter

from .views import LoginAPIView, RegistrationAPIView, ProductView, RestaurantView


router = DefaultRouter()
router.register('product', ProductView, basename='product')
router.register('restaurants', RestaurantView, basename='restaurants')

urlpatterns = [
    re_path(r'^registration/?$', RegistrationAPIView.as_view(), name='user_registration'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),
]

urlpatterns += router.urls
