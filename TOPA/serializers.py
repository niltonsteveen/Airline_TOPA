from rest_framework import serializers
from .models import Airline, Flight

class AirlineSerializer(serializers.ModelSerializer):
	
	class Meta:
		model=Airline
		fields=('code','name','thumbnail')

class FlightSerializer(serializers.ModelSerializer):
	
	class Meta:
		model=Flight
		fields=('airline','flightCode','origin','destination','price','currency','date','roundTrip')