from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	age = models.IntegerField()
	phone = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	# confirmpassword = models.CharField(max_length=100)
	
class Flight(models.Model):
	origin = models.CharField(max_length=100)
	destination = models.CharField(max_length=100)
	departure = models.DateTimeField()
	arrival = models.DateTimeField()
	price = models.IntegerField()
	fligh_number = models.CharField(max_length=100)
	vacant_seats = models.IntegerField()
	# passenger = models.ForeignKey(User, on_delete=models.CASCADE)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
	flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
	seat_number = models.IntegerField()
	is_available = models.BooleanField(default=True)
    
