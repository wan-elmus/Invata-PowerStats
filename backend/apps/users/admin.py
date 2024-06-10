from django.contrib import admin
from .models import CustomUser, BatteryConsumption, PowerConsumption, Payment, ChargingStatus, Uptime

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(BatteryConsumption)
admin.site.register(PowerConsumption)
admin.site.register(Payment)
admin.site.register(ChargingStatus)
admin.site.register(Uptime)