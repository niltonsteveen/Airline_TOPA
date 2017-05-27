from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import Airline, Flight
from .serializers import AirlineSerializer, FlightSerializer
from rest_framework.decorators import api_view
from django.db.models import Q
import json
from django.core import serializers
import datetime
# Create your views here.

@api_view(['POST','GET'])
def ejemplo(request):
	if request.method == 'POST':
		data=request.data
		fecha=data['departureDate']
		fechaStr=datetime.datetime.strptime(fecha, "%d-%m-%Y")
		ano=fechaStr.year
		mes=fechaStr.month
		dia=fechaStr.day
	#	lista=[{ 'airline':{'code':'2215','name':'TOPA', 'thumbnail':'http://shmector.com/_ph/12/221844079.png'}, }]
		flights = Flight.objects.filter(origin=data['origin'], destination=data['destination'],date__day=dia, date__month=mes, date__year=ano)		
		if data['roundTrip']:
			fecha2=data['arrivalDate']
			fechaStr2=datetime.datetime.strptime(fecha2, "%d-%m-%Y")
			ano2=fechaStr2.year
			mes2=fechaStr2.month
			dia2=fechaStr2.day
			flights = Flight.objects.filter(Q(origin=data['origin'],destination=data['destination'], date__day=dia, date__month=mes, date__year=ano) | Q(origin=data['destination'], destination=data['origin'],date__day=dia2, date__month=mes2, date__year=ano2))		
		serializer=FlightSerializer(flights, many=True)
		#res = '{ "airline":{"code":"2215","name":"TOPA", "thumbnail":"http://shmector.com/_ph/12/221844079.png"}, "results":'+datoserializado+'}'
		#res1=json.dumps({ "airline":{"code":"2215","name":"TOPA", "thumbnail":"http://shmector.com/_ph/12/221844079.png"}, "results":res)
		return Response(data={"airline":{"code":"2215","name":"TOPA", "thumbnail":"http://shmector.com/_ph/12/221844079.png"}, "results": serializer.data})
	elif request.method == 'GET':
		flights = Flight.objects.all()
		serializer = FlightSerializer(flights, many=True)
		return Response(serializer.data)
