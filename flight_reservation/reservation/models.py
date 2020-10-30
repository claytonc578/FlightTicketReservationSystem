from django.db import models
from django.contrib.auth.models import User #import the sender
from django.urls import reverse

class Plane(models.Model):
    plane_number = models.IntegerField(default=0)
    rows = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    reserved = models.IntegerField(default=0)

    def __str__(self):
        return "Plane {}".format(self.plane_number)

class Flight(models.Model):
    flight_number = models.IntegerField(default=0)
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    plane = models.OneToOneField(Plane, on_delete=models.CASCADE)

    def __str__(self):
        return "Flight {}".format(self.flight_number)

class Ticket(models.Model):
    # def row_choice_gen(self, rows):
    #     for row in rows:
    #         row_choices.append(row)
    #     return row_choices
    #
    # def column_choice_gen(self, cols):
    #     for col in cols:
    #         col_choices.append(chr(col+65))
    #     return col_choices

    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    # @property
    # def plane_rows(self):
    #     return self.flight.plane.rows
    #
    # @property
    # def plane_width(self):
    #     return self.flight.plane.width


    # ROW_CHOICES = row_choice_gen(plane_rows())
    # COL_CHOICES = row_choice_gen(plane_width())

    row = models.IntegerField(default=1)
    column = models.CharField(max_length=1, default="A")
    first_name = models.CharField(max_length=200, default="")
    last_name = models.CharField(max_length=200, default="")
    passenger = models.ForeignKey(User, on_delete = models.SET_NULL, blank=True, null=True) #cascade: if user is deleted, delete profile, but if profile delete, user not deleted

    def __str__(self):
        return "Flight #{}; {} to {} Passenger: {} {}".format(self.flight.flight_number,
                        self.flight.origin, self.flight.destination, self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('flight-detail', kwargs = {'pk': self.pk}) #reverse: return full path as string
