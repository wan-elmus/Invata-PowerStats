from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import ConsumptionData
from .serializers import ConsumptionDataSerializer


class ConsumptionDataListView(generics.ListAPIView):
    queryset = ConsumptionData.objects.all()
    serializer_class = ConsumptionDataSerializer
    permission_classes = [IsAuthenticated]

# Other views related to consumption data can be added here.

