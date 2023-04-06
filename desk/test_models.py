from django.test import TestCase
from .models import Booking, Enquiry
from django.contrib.auth.models import User
from django.db.models import (ForeignKey, CharField, EmailField)


class BookingTests(TestCase):
    """
    Test user booking
    """

    def setUp(self):
        self.client = User.objects.create(
            email='test@example.com',
            password='testpasswd')


class EnquiryTest(TestCase):
    def setUp(self):
        self.enquiry = Enquiry.objects.create(
            name='john',
            subject='text')

    def test_enquiry_str(self):
        enquiry_name = str(self.enquiry.name)
        enquiry_subject = str(self.enquiry.subject)
        self.assertEqual(str(self.enquiry), f"from {enquiry_name} | subject: {enquiry_subject}")


    # def test_fun(self):
    #     booking = self.get_object()
    #     if self.request.user == client.id:
    #         return True
    #     return False
