from django.test import TestCase
from django.utils import timezone
from users.models import CustomUser
from .models import ConsumptionData


class ConsumptionDataTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='test@example.com',
            first_name='Test',
            last_name='User',
            password='testpass123'
        )
        self.consumption_data = ConsumptionData.objects.create(
            user=self.user,
            consumption=20.00,
            date_recorded=timezone.now()
        )

    def test_consumption_data_str(self):
        """
        Test the __str__() method of ConsumptionData model
        """
        expected_str = f"{self.user.email} - {self.consumption_data.consumption} kWh - {self.consumption_data.date_recorded}"
        self.assertEqual(str(self.consumption_data), expected_str)

