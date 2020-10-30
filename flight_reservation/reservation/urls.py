from django.urls import path
from .views import (FlightListView,
                    FlightDetailView,
                    TicketCreateView)

from . import views

urlpatterns = [
    path('', FlightListView.as_view(), name='reservation-home'),
    path('about/', views.about, name='reservation-about'),
    path('reserve/', views.reserve, name='reservation-reserve'),
    path('reservation/new/', TicketCreateView.as_view(), name='reservation-create'),
    path('flight/<int:pk>/', FlightDetailView.as_view(), name='flight-detail'), #end routes with trailing /
]
