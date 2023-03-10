from django.shortcuts import render
from django.views import generic
from .models import Booking


class BookingListView(generic.ListView):
    """
    View for displaying booking availability.
    """
    model = Booking
    queryset = Booking().objects.filter(client=self.request.user)
    template_name = 'spaces.html'
    context_object_name = 'spaces'
    paginate_by = 4

