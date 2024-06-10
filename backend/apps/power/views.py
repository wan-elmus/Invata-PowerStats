from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import PowerData
from .serializers import PowerDataSerializer


class PowerDataListView(generics.ListAPIView):
    queryset = PowerData.objects.all()
    serializer_class = PowerDataSerializer
    permission_classes = [IsAuthenticated]

# Other views related to power data can be added here.
