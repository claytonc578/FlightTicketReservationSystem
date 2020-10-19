from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='reservation-home'),
    path('about/', views.about, name='reservation-about'),
]
