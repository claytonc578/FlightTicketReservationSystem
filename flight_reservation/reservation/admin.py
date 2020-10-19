from django.contrib import admin

from .models import Passenger, Plane, Flight

admin.site.register(Passenger)
admin.site.register(Plane)
admin.site.register(Flight)
