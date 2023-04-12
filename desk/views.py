from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib import messages
from desk.models import Booking, Service, Enquiry
from .forms import BookingForm, ContactForm
from django.views.generic.edit import FormView, UpdateView, DeleteView


class HomePageView(TemplateView):
    """
    View for home page.
    """
    template_name = 'home/index.html'


class ContactFormView(FormView):
    """
    View for users ContactForm
    """
    model = Enquiry
    form_class = ContactForm
    template_name = 'home/index.html'

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            contact_form = self.form_class(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                messages.success(
                    self.request,
                    'Thank you for contacting DESK HQ. We recieved your message, will get back to you shortly.')
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.info(
                    self.request,
                    'This field is required')
                # return HttpResponseRedirect(reverse('home'))
                return HttpResponse("")


class BookingsList(ListView):
    """
    View for users Booking
    """
    model = Booking
    template_name = 'desk/booking_details.html'
    context_object_name = 'bookings'
    paginate_by = 4

    def get_queryset(self):
        return Booking.objects.filter(client=self.request.user)


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
                    'Thank you for using DESK HQ. Your Booking was created successfully.')
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.add_message(
                    request,
                    messages.INFO,
                    'Sorry!, A signin is required first.')
                return HttpResponseRedirect(reverse('account_login'))
        else:
            return self.form_invalid(form)


class BookingUpdateView(UpdateView):
    """
    View allows user to edit and update their booking and
    redirects them to booking details.
    """
    model = Booking
    form_class = BookingForm
    template_name = 'desk/update_booking.html'
    success_url = reverse_lazy('booking_details')

    def get_object(self, queryset=None):
        """
        Retrieve the object to be updated, using the primary key from the URL
        """
        booking = get_object_or_404(Booking, pk=self.kwargs['pk'])
        return booking

    def form_valid(self, form):
        messages.success(self.request, 'Booking updated successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            'Booking update failed. Please check the form and try again.')
        return super().form_invalid(form)


class BookingDeleteView(DeleteView):
    """
    View allow user to delete booking and redirect user to booking details.
    """
    model = Booking
    template_name = 'desk/delete_booking.html'
    success_url = reverse_lazy('booking_details')

    def get_object(self, queryset=None):
        """
        Retrieve the object to be deleted, using the primary key from the URL
        """
        booking_detail = get_object_or_404(Booking, pk=self.kwargs['pk'])
        return booking_detail

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Booking deleted successfully!')
        return super().form_valid(form)


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
