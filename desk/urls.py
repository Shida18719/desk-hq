from django.urls import path
from . import views

# Urls for app views
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    # path('book_space/', views.BookingFormView.as_view(), name='book_space'),
    path('space_booking/', views.BookingFormView.as_view(), name='space_booking'),
    path('about_us/', views.AboutView.as_view(), name="about_us"),
]
