from django.contrib import admin
from .models import Registration, Location, Space_type, Booking


# Registion for further enquiries
admin.site.register(Registration)


# Workspace location.
@admin.register(Location)
class WorkSpaceAdmin(admin.ModelAdmin):

    list_display = ('location_name', 'address', 'capacity')
    search_fields = ('location_name', 'capacity')


# Space type facility
@admin.register(Space_type)
class SpaceTypeAdmin(admin.ModelAdmin):

    list_display = ('name', 'space', 'capacity')
    search_fields = ('name', 'space', 'capacity')
    list_filter = ('name', 'capacity')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        'client', 'space_booking', 'booking_date', 'booking_duration', 
        'booking_time', 'end_time')
    search_fields = ('client', 'space_booking')
    list_filter = (
        'space_booking', 'booking_date', 'booking_duration', 'booking_time')
