from django.contrib import admin
from .models import Registration, Location, Service, Booking


# Registion for further enquiries
admin.site.register(Registration)


# Workspace location.
@admin.register(Location)
class WorkSpaceAdmin(admin.ModelAdmin):

    list_display = ('location_name', 'slug', 'address', 'featured_image')
    prepopulated_fields = {'slug': ('location_name',)}
    list_filter = ('location_name', 'address')
    search_fields = ('location_name', 'address')


# Space type facility
@admin.register(Service)
class SpaceTypeAdmin(admin.ModelAdmin):

    list_display = ('name', 'capacity')
    search_fields = ('name', 'capacity')
    list_filter = ('name', 'capacity')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        'client', 'space_booking', 'booking_date', 'booking_duration', 
        'booking_start', 'booking_end', 'approved')
    search_fields = ('client', 'space_booking')
    list_filter = (
        'space_booking', 'booking_date', 'booking_duration',
        'booking_start', 'approved')
    actions = ['approve_booking_cancellation']

    def approve_booking_cancellation(self, request, queryset):
        queryset.update(approved=True)
