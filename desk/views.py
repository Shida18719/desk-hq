from django.shortcuts import render
from django.views import generic
from .models import Booking


class BookingListView(generic.ListView):
    """
    View for displaying booking availability.
    """
    model = Booking
    template_name = 'spaces.html'
    context_object_name = 'spaces'
    paginate_by = 4

    def get_queryset(self):
        """
        Filters bookings for the current user
        """
        return Booking.objects.filter(client=self.request.user)
