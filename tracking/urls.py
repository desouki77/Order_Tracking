from django.urls import path
from .views import OrderTracking

urlpatterns = [
    path('orders/', OrderTracking.as_view(), name='order-tracking')
]