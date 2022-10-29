# import http response
from django.shortcuts import render
from django.http import HttpResponse

# import user
from .models import User

# Create your views here.

# home page function
def index(request):
	return render(request, "index.html")

def about(request):
	return render(request, "about.html")

def createUser(request):
	# read data from html and add to User
	name = request.POST.get('name')
	email = request.POST.get('email')
	password = request.POST.get('password')
	phone = request.POST.get('phone')
	age = request.POST.get('age')
	# create user
	user = User(name=name, email=email, password=password, phone=phone, age=age)
	user.save()

def displayAvailableFlights(request):
	# get all flights
	flights = Flight.objects.all()
	# render html
	return render(request, "flights.html", {"flights": flights})

def bookFlight(request):
	# get flight id
	flight_id = request.POST.get("flight_id")
	# get flight
	flight = Flight.objects.get(id=flight_id)
	# get user
	user = User.objects.get(id=1)
	# create booking
	booking = Booking(user=user, flight=flight)
	booking.save()
	# render html
	return render(request, "booking.html", {"booking": booking})