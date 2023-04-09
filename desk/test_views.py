from django.test import TestCase, RequestFactory, Client
# from django.views.generic.edit import FormView, UpdateView, DeleteView
from .views import ContactFormView
from .forms import ContactForm
from desk.models import Booking, Enquiry
from django.urls import reverse
from django.contrib.messages import get_messages
from django.http import HttpRequest, HttpResponse


class ContactFormViewTest(TestCase):
    """
    Test ContactFormView  
    """
    def setUp(self):
        self.factory = RequestFactory()

    def test_valid_form_submission(self):
        """
        Test that the contactform  data creates valid data, if a valid form
        submission is successful, the form data is saved to the database,
        and the success message is displayed.
        """
        response = self.client.post('/', {
            'name': 'Test',
            'email': 'test@example.com',
            'subject': 'Text subject',
            'message': 'This is a message'
        })

        # check if the form submission was successful
        self.assertEqual(response.status_code, 302)

        self.assertTrue(Enquiry.objects.filter(name='Test', subject='Text subject').exists())

        # check if the success message was displayed
        messages = get_messages(response.wsgi_request)
        self.assertIn(
            'Thank you for contacting DESK HQ. We recieved your message, will get back to you shortly.',
            [str(message) for message in messages])

    def test_invalid_form_submission(self):
        """
        Tests if an invalid form submission fails, the form data is not saved
        to the database, and the form errors are displayed.
        """
        response = self.client.post('/', {
            'name': '',
            'email': 'test@example.com',
            'subject': 'Text message',
            'message': 'This is a message',
        })

        # check if the form submission failed
        self.assertEqual(response.status_code, 200)

        # check if the form data was not saved to the database
        self.assertFalse(Enquiry.objects.filter(email='test@example.com', subject='Text message').exists())

        # check if the form errors were displayed
        self.assertContains(response, '')


class BookingsListTest(TestCase):
    """
    View for users Booking
    """