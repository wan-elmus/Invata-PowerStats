
from rest_framework import serializers
from .models import ConsumptionData


class ConsumptionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsumptionData
        fields = ['id', 'user', 'consumption', 'date_recorded']
