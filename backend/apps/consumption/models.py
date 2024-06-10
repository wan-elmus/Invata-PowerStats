from django.db import models
from users.models import CustomUser


class ConsumptionData(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    consumption = models.DecimalField(max_digits=10, decimal_places=2)
    date_recorded = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.consumption} kWh - {self.date_recorded}"
