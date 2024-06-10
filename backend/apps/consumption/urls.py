
from django.urls import path
from .views import ConsumptionDataListView

urlpatterns = [
    path('consumption/', ConsumptionDataListView.as_view(), name='consumption-data-list'),
    # Add other URL patterns related to consumption data here.
]
