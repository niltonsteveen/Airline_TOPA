from django.db import models

# Create your models here.

class Airline(models.Model):
	code=models.CharField(max_length=20, primary_key=True)
	name=models.CharField(max_length=30)
	thumbnail=models.CharField(max_length=1000)

	def __str__(self):
		return self.name

class Flight(models.Model):
	flightCode=models.CharField(max_length=15, primary_key=True)
	origin=models.CharField(max_length=30)
	destination=models.CharField(max_length=30)
	price=models.IntegerField()
	currency=models.CharField(max_length=8)
	date=models.DateTimeField()
	roundTrip=models.NullBooleanField()
	airline=models.CharField(max_length=20)

	def __str__(self):
		return self.flightCode