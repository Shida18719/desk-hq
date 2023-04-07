from django.test import TestCase
from .models import Booking, Enquiry, Location
from django.contrib.auth.models import User
from django.db.models import (ForeignKey, CharField, EmailField, IntegerField)


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
        self.assertEqual(
            str(self.enquiry), f"from {enquiry_name} | subject: {enquiry_subject}")


class LocationTest(TestCase):
    def setUp(self):
        reset_sequences = True
        self.location1 = Location.objects.create(
            location_name='DESK HQ Brooklyn House (3 STONE AVENUE LONDON SE5 2AZ')
    
    def test_location_name(self):
        """Test string representation of the location_name"""
        location1 = str(self.location1.location_name)
        self.assertEqual(str(self.location1), (location1))
        self.assertTrue(self.location1)

    # def test_fun(self):
    #     booking = self.get_object()
    #     if self.request.user == client.id:
    #         return True
    #     return False
