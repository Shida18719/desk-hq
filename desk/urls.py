from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('book_space/', views.BookingFormView.as_view(), name='book_space'),
]
