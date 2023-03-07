from django.contrib import admin
from .models import Registration, Work_space


# Registion for further enquiries
admin.site.register(Registration)


# Workspace location.
@admin.register(Work_space)
class Work_space():
    