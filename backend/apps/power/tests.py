from django.test import TestCase
from django.utils import timezone
from users.models import CustomUser
from .models import PowerData


class PowerDataTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='test@example.com',
            first_name='Test',
            last_name='User',
            password='testpass123'
        )
        self.power_data = PowerData.objects.create(
            user=self.user,
            consumption=50.00,
            date_recorded=timezone.now()
        )

    def test_power_data_str(self):
        self.assertEqual(str(self.power_data), "test@example.com - 50.00 kWh - " + str(self.power_data.date_recorded))
