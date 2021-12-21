from rest_framework.routers import DefaultRouter
0
from .views import ProductOrderView, ProductView, RestaurantView

router = DefaultRouter()
router.register('product', ProductView)
router.register('restaurant', RestaurantView)
router.register('order', ProductOrderView)

urlpatterns = router.urls
