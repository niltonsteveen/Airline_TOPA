from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import Airline, Flight
from .serializers import AirlineSerializer, FlightSerializer
from rest_framework.decorators import api_view
from django.db.models import Q
import json
# Create your views here.

@api_view(['POST','GET'])
def ejemplo(request):
	if request.method == 'POST':
		data=request.data
	#	lista=[{ 'airline':{'code':'2215','name':'TOPA', 'thumbnail':'http://shmector.com/_ph/12/221844079.png'}, }]
		flights = Flight.objects.filter(flightCode=data['flightCode'], origin=data['origin'], destination=data['destination'],
			price=data['price'], currency=data['currency'], date=data['date'], passengers=data['passengers'])		
		if data['roundTrip']:
			flights = Flight.objects.filter(Q(flightCode=data['flightCode'], origin=data['origin'], destination=data['destination'],
			price=data['price'], currency=data['currency'], date=data['date'], passengers=data['passengers']) | Q(origin=data['destination'], destination=data['origin']))
		serializer = '{ "airline":{"code":"2215","name":"TOPA", "thumbnail":"http://shmector.com/_ph/12/221844079.png"}, "results":'+FlightSerializer(flights, many=True)+'}'
		res=json.dumps(serializer)
		return Response(res)
	elif request.method == 'GET':
		flights = Flight.objects.all()
		serializer = FlightSerializer(flights, many=True)
		return Response(serializer.data)
