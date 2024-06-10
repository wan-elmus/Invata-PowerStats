from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics, permissions
from .models import CustomUser, BatteryConsumption, PowerConsumption, Payment, ChargingStatus, Uptime
from .serializers import (
    CustomUserSerializer,
    BatteryConsumptionSerializer,
    PowerConsumptionSerializer,
    PaymentSerializer,
    ChargingStatusSerializer,
    UptimeSerializer
)


class IsAdminUser(permissions.BasePermission):
    """
    Custom permission to allow access only to admin users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_admin

# CustomUser Views
class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_admin:
            return CustomUser.objects.all()  # Admin can see all users
        else:
            return CustomUser.objects.filter(id=user.id)  # Regular user can only see their own details

# BatteryConsumption Views
class BatteryConsumptionListCreate(generics.ListCreateAPIView):
    queryset = BatteryConsumption.objects.all()
    serializer_class = BatteryConsumptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# PowerConsumption Views
class PowerConsumptionListCreate(generics.ListCreateAPIView):
    queryset = PowerConsumption.objects.all()
    serializer_class = PowerConsumptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Payment Views
class PaymentListCreate(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# ChargingStatus Views
class ChargingStatusListCreate(generics.ListCreateAPIView):
    queryset = ChargingStatus.objects.all()
    serializer_class = ChargingStatusSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Uptime Views
class UptimeListCreate(generics.ListCreateAPIView):
    queryset = Uptime.objects.all()
    serializer_class = UptimeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


