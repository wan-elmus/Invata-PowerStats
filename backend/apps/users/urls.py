from django.urls import path
from .views import (
    UserListCreateView,
    UserDetailView,
    BatteryConsumptionListCreate,
    PowerConsumptionListCreate,
    PaymentListCreate,
    ChargingStatusListCreate,
    UptimeListCreate
)

urlpatterns = [
    # User URLs
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    # Battery Consumption URL
    path('battery-consumption/', BatteryConsumptionListCreate.as_view(), name='battery-consumption-list-create'),

    # Power Consumption URL
    path('power-consumption/', PowerConsumptionListCreate.as_view(), name='power-consumption-list-create'),

    # Payment URL
    path('payments/', PaymentListCreate.as_view(), name='payment-list-create'),

    # Charging Status URL
    path('charging-status/', ChargingStatusListCreate.as_view(), name='charging-status-list-create'),

    # Uptime URL
    path('uptime/', UptimeListCreate.as_view(), name='uptime-list-create'),
]
