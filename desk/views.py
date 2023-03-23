from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib import messages

# Booking
from desk.models import Booking, Service
from .forms import BookingForm
from django.views.generic.edit import FormView


class HomePageView(TemplateView):
    """
    View for home page.
    """
    template_name = 'home/index.html'


class BookingListView(ListView):
    """
    View for users Booking
    """
    model = Booking
    form_class = BookingForm
    template_name = 'desk/booking_details.html'
    context_object_name = 'list'
    paginate_by = 4

    def get_queryset(self):
        return Booking.objects.filter(client=self.request.user.id)


class BookingFormView(FormView):
    """
    View for displaying booking availability and allow user to create booking.
    """
    form_class = BookingForm
    template_name = 'desk/space_booking.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            if self.request.user.is_authenticated:
                form.instance.client = request.user
            # <process form cleaned data>
                form.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Your Booking has been created successfully.')
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.add_message(
                    request,
                    messages.INFO,
                    'Sorry!, A signin is required first.')
                return HttpResponseRedirect(reverse('account_login'))
        else:
            return self.form_invalid(form)

        # return render(request, self.template_name, {'form': form})


class AboutView(TemplateView):
    """
    View for about_us page
    """
    template_name = 'home/about_us.html'


class ServiceListView(ListView):
    """
    View for services page
    """
    template_name = 'home/services.html'
    queryset = Service.objects.order_by('-timestamp')
    context_object_name = 'services'
