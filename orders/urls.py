from django.urls import path,include
from .views import OrdersViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'orders',OrdersViewSet,basename="order")


urlpatterns = [
    path('',include(router.urls)),
]