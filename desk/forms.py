from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    Create BookingForm
    """

    class Meta:
        model = Booking
        fields = [
            'client', 'location', 'space_booking', 'booking_date',
            'booking_duration', 'booking_start', 'booking_end']
