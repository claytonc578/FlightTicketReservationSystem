from django.contrib import admin

from .models import Plane, Flight, Ticket

admin.site.register(Plane)
admin.site.register(Flight)
admin.site.register(Ticket)
