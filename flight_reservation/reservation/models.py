from django.db import models

class Passenger(models.Model):
    row = models.IntegerField(default=0)
    col = models.CharField(max_length=1)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Plane(models.Model):
    plane_number = models.IntegerField(default=0)
    rows = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    reserved = models.IntegerField(default=0)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)

    def __str__(self):
        return "Plane {}".format(self.plane_number)

class Flight(models.Model):
    flight_number = models.IntegerField(default=0)
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    plane = models.OneToOneField(Plane, on_delete=models.CASCADE)

    def __str__(self):
        return "Flight {}".format(self.flight_number)
