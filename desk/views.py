from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy

# Booking
from .models import Booking
from .forms import BookingForm
from django.views.generic.edit import FormView


class HomePageView(TemplateView):
    """
    View for home page.
    """
    template_name = 'home/index.html'

# def home_page(request):
#     return render(request, 'index.html')


class BookingFormView(FormView):
    """
    View for displaying booking availability.
    """
    model = Booking
    form_class = BookingForm
    template_name = 'desk/space_booking.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})


class AboutView(TemplateView):
    """
    View for about_us page
    """
    template_name = 'home/about_us.html'
    # success_url = reverse_lazy('space')

    # def get_queryset(self):
    #     """
    #     Filters bookings for the current user
    #     """
    #     return Booking.objects.filter(client=self.request.user)
