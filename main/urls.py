from django.urls import re_path
from rest_framework.routers import DefaultRouter

from .views import (LoginAPIView, ProductView, RegistrationAPIView,
                    RestaurantView)

router = DefaultRouter()
router.register('product', ProductView, basename='product')
router.register('restaurant', RestaurantView, basename='restaurant')

urlpatterns = [
    re_path(r'^registration/?$', RegistrationAPIView.as_view(), name='user_registration'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),
]

urlpatterns += router.urls
