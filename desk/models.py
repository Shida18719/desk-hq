from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from cloudinary.models import CloudinaryField


class Registration(models.Model):
    """
    User model contact for enquires.
    """

    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


# Office space locations
OFFICE_LOCATION = [
    ('DESK HQ Brooklyn House', 'DESK HQ Brooklyn House'),
    ('DESK HQ Dockyard Place', 'DESK HQ Dockyard Place'),
]


# Create field choices for Services Offered
SERVICES = [
    ('Day WorkStation', 'Day WorkStation'),
    ('Conference Room(Up to 35 seats)', 'Conference Room(Up to 35 seats)'),
    ('Coworking WorkStation', 'Coworking WorkStation'),
    ('Exclusive workstation(private)', 'Exclusive workstation(private)'),
    ('Training Rooms', 'Training Rooms'),
    ('Meeting Room(Up to 12 seats)', 'Meeting Room(Up to 12 seats)'),
]


# Duration
DURATION = [
    ('1 Hour', '1 Hour'),
    ('2 Hours', '2 Hours'),
    ('3 Hours', '3 Hours'),
    ('4 Hours', '4 Hours'),
    ('5 Hours', '5 Hours'),
    ('6 Hours', '6 Hours'),
    ('7 Hours', '7 Hours'),
    ('8 Hours', '8 Hours'),
    ('All day', 'All day'),
]


# Booking Times
HOURS = [
    ("09:00 am", "09:00 am"),
    ("09:30 am", "09:30 am"),
    ("10:00 am", "10:00 am"),
    ("10:30 am", "10:30 am"),
    ("11:00 am", "11:00 am"),
    ("11:30 am", "11:30 am"),
    ("12:00 pm", "12:00 pm"),
    ("12:30 pm", "12:30 pm"),
    ("13:00 pm", "13:00 pm"),
    ("13:30 pm", "13:30 pm"),
    ("14:00 pm", "14:00 pm"),
    ("14:30 pm", "14:30 pm"),
    ("15:00 pm", "15:00 pm"),
    ("15:30 pm", "15:30 pm"),
    ("16:00 pm", "16:00 pm"),
    ("16:30 pm", "16:30 pm"),
    ("17:00 pm", "17:00 pm"),
    ("17:30 pm", "17:30 pm"),
]


# Create entry
# for specific workspace and location
class Location(models.Model):

    location_name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=200, unique=True)
    capacity = models.CharField(
        max_length=50,
        choices=OFFICE_LOCATION,
        unique=True)

    class Meta:
        ordering = ['location_name']

    def __str__(self):
        return self.name

    def __str__(self):
        return f"{self.capacity}"


class Space_type(models.Model):

    name = models.CharField(max_length=100, unique=True)
    space = models.ForeignKey(
        Location, on_delete=models.CASCADE,
        related_name='space_type', default='')
    capacity = models.CharField(
        max_length=50,
        choices=SERVICES,
        unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def __str__(self):
        return f"{self.capacity}"


class Booking(models.Model):
    """
    Customer booking system
    """
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='client_booking')
    space_booking = models.ForeignKey(
        Space_type, on_delete=models.CASCADE, related_name='space_booking',
        default='')
    booking_date = models.DateField(default=datetime.now)
    booking_duration = models.CharField(
        max_length=20,
        choices=DURATION,
        default="Anytime")
    booking_time = models.CharField(
        max_length=20,
        choices=HOURS,
        default="09:00 am")
    end_time = models.DateTimeField()

    class Meta:
        # ordering = ['booking_duration']
        order_with_respect_to = 'space_booking'

    def __str__(self):
        return f"{self.client} booked {self.space_booking} | {self.booking_date} | {self.booking_time}"
