from django.urls import re_path
from rest_framework.routers import DefaultRouter
0
from .views import (LoginAPIView, ProductOrderView, ProductView, RegistrationAPIView,
                    RestaurantView)

router = DefaultRouter()
router.register('product', ProductView, basename='product')
router.register('restaurant', RestaurantView, basename='restaurant')
router.register('order', ProductOrderView, basename='order')

urlpatterns = [
    re_path(r'^registration/?$', RegistrationAPIView.as_view(), name='user_registration'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),
]

urlpatterns += router.urls
