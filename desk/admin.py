from django.contrib import admin
from .models import Registration, Location, Service, Booking


# Registion for further enquiries
admin.site.register(Registration)


# Workspace location.
@admin.register(Location)
class WorkSpaceAdmin(admin.ModelAdmin):

    list_display = ('location_name', 'slug', 'featured_image')
    prepopulated_fields = {'slug': ('location_name',)}
    list_filter = ('location_name',)
    search_fields = ('location_name',)


# Space type facility
@admin.register(Service)
class SpaceTypeAdmin(admin.ModelAdmin):

    list_display = ('space_type',)
    search_fields = ('space_type',)
    list_filter = ('space_type',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        'client', 'location', 'space_booking', 'booking_date',
        'booking_duration',
        'booking_start', 'booking_end', 'created_on', 'status', 'approved')
    search_fields = ('client', 'location', 'space_booking')
    list_filter = (
        'space_booking', 'location', 'booking_date', 'booking_duration',
        'booking_start', 'created_on', 'status', 'approved')
    actions = ['approve_booking_cancellation']

    def approve_booking_cancellation(self, request, queryset):
        queryset.update(approved=True)
