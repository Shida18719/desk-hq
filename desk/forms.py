from django import forms
from .models import Booking, Location


class BookingForm(forms.ModelForm):
    """
    Create BookingForm
    """

    OFFICE_LOCATION = [
        ('DESK HQ Brooklyn House (3 STONE AVENUE LONDON SE5 2AZ)',
            'DESK HQ Brooklyn House (3 STONE AVENUE LONDON SE5 2AZ)'),
        ('DESK HQ Dockyard Place (55 PARADE STREET LONDON E20 3YB)',
            'DESK HQ Dockyard Place (55 PARADE STREET LONDON E20 3YB)'),
    ]

    SERVICES = [
        ('Day WorkStation', 'Day WorkStation'),
        ('Conference Room(Up to 35 seats)', 'Conference Room(Up to 35 seats)'),
        ('Coworking WorkStation', 'Coworking WorkStation'),
        ('Exclusive workstation(private)', 'Exclusive workstation(private)'),
        ('Training Rooms', 'Training Rooms'),
        ('Meeting Room(Up to 12 seats)', 'Meeting Room(Up to 12 seats)'),
    ]

    location = forms.ChoiceField(
        choices=OFFICE_LOCATION, widget=forms.Select)

    space_booking = forms.ChoiceField(
        choices=SERVICES, widget=forms.Select)

    class Meta:
        model = Booking
        fields = [
            'location', 'space_booking', 'booking_date',
            'booking_duration', 'booking_start', 'booking_end']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'})
        }
