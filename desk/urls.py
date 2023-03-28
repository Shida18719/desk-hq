from django.urls import path
from . import views
from .views import BookingDeleteView

# Urls for app views
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    # path('locations/<slug:slug>/', views.BookingFormView.as_view(), name='space_booking'),

    path('space_booking/', views.BookingFormView.as_view(), name='space_booking'),
    path('about_us/', views.AboutView.as_view(), name="about_us"),
    path('services/', views.ServiceListView.as_view(), name="services"),
    path('booking_details/', views.BookingsList.as_view(), name="booking_details"),
    path('booking_details/<pk>/update', views.BookingUpdateView.as_view(), name="update_booking"),
    path('delete_booking/<int:pk>', BookingDeleteView.as_view(), name="cancelBooking"),
]
