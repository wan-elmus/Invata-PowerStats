
from django.urls import path
from .views import PowerDataListView

urlpatterns = [
    path('power/', PowerDataListView.as_view(), name='power-data-list'),
    # Add other URL patterns related to power data here.
]
