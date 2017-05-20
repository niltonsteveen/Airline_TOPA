from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import Airline, Flight
from .serializers import AirlineSerializer, FlightSerializer
from rest_framework.decorators import api_view
from django.db.models import Q
import json
from django.core import serializers
# Create your views here.

@api_view(['POST','GET'])
def ejemplo(request):
	if request.method == 'POST':
		data=request.data


	#	lista=[{ 'airline':{'code':'2215','name':'TOPA', 'thumbnail':'http://shmector.com/_ph/12/221844079.png'}, }]
		flights = Flight.objects.filter(origin=data['origin'], destination=data['destination'],
			currency=data['currency'], date__contains=datetime.strptime(data['departureDate'], '%Y-%m-%d'))		
		if data['roundTrip']:
			flights = Flight.objects.filter(Q(origin=data['origin'], destination=data['destination'],
			currency=data['currency'], date=data['departureDate']) | Q(origin=data['destination'], destination=data['origin'], date=data['arrivalDate']))
		serializer=FlightSerializer(flights, many=True)
		
		#res = '{ "airline":{"code":"2215","name":"TOPA", "thumbnail":"http://shmector.com/_ph/12/221844079.png"}, "results":'+datoserializado+'}'
		#res1=json.dumps({ "airline":{"code":"2215","name":"TOPA", "thumbnail":"http://shmector.com/_ph/12/221844079.png"}, "results":res)
		return Response(data={"airline":{"code":"2215","name":"TOPA", "thumbnail":"http://shmector.com/_ph/12/221844079.png"}, "results": serializer.data})
	elif request.method == 'GET':
		flights = Flight.objects.all()
		serializer = FlightSerializer(flights, many=True)
		return Response(serializer.data)
