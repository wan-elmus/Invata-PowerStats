
from django.test import TestCase
from django.utils import timezone
from users.models import CustomUser
from .models import Payment


class PaymentTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='test@example.com',
            first_name='Test',
            last_name='User',
            password='testpass123'
        )
        self.payment = Payment.objects.create(
            user=self.user,
            amount=100.00,
            date_paid=timezone.now()
        )

    def test_payment_str(self):
        self.assertEqual(str(self.payment), "test@example.com - $100.00 - " + str(self.payment.date_paid))
