
from rest_framework import serializers
from .models import CustomUser, BatteryConsumption, PowerConsumption, Payment, ChargingStatus, Uptime

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'is_admin']

class BatteryConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatteryConsumption
        fields = ['id', 'user', 'timestamp', 'value']

class PowerConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerConsumption
        fields = ['id', 'user', 'timestamp', 'value']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'user', 'amount', 'timestamp']

class ChargingStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargingStatus
        fields = ['id', 'user', 'percentage', 'timestamp']

class UptimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uptime
        fields = ['id', 'user', 'uptime', 'timestamp']
