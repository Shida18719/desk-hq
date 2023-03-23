from django.urls import path
from . import views

# Urls for app views
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    # path('locations/<slug:slug>/', views.BookingFormView.as_view(), name='space_booking'),

    path('space_booking/', views.BookingFormView.as_view(), name='space_booking'),
    path('about_us/', views.AboutView.as_view(), name="about_us"),
    path('services/', views.ServiceListView.as_view(), name="services"),
    path('booking_details/', views.BookingsList.as_view(), name="booking_details"),
]
