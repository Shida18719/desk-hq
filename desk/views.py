from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.urls import reverse_lazy

# Booking
from desk.models import Booking, Service
from .forms import BookingForm
from django.views.generic.edit import FormView


class HomePageView(TemplateView):
    """
    View for home page.
    """
    template_name = 'home/index.html'


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


class ServiceListView(ListView):
    """
    View for services page
    """
    template_name = 'home/services.html'
    queryset = Service.objects.order_by('-timestamp')
    context_object_name = 'services'
