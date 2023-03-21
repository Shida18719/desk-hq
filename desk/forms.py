from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    Create BookingForm
    """

    class Meta:
        model = Booking
        fields = [
            'location', 'space_booking', 'booking_date',
            'booking_duration', 'booking_start', 'booking_end']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'})
        }
