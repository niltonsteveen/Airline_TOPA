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
from django.views.generic.base import TemplateView
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import os.path
from pyrebase import pyrebase
from rest_framework import generics
import json
from datetime import datetime, date, time, timedelta
import calendar

# Create your views here.

class InicioView(TemplateView):
	template_name="web/index.html"

class opciones:
	default_app = None
	config = {
		"apiKey": "AIzaSyAgpcndOPW3Yk7pprbxZyQp1Oq_ln9Y0vw",
		"authDomain": "python-project-de5a9.firebaseapp.com",
		"databaseURL": "https://python-project-de5a9.firebaseio.com/",
		"storageBucket": "python-project-de5a9.appspot.com"
	}

	firebase=None
	db = None
	def setCredencial(arg):
		opciones.default_app=arg

	def getCredencial():
		return default_app

	def setConfigDatabase():
		opciones.firebase = pyrebase.initialize_app(opciones.config)

	def setDataBase():
		opciones.db=opciones.firebase.database()

	def getDataBase():
		return opciones.db

	def loadService():
		module_dir = os.path.dirname(__file__)  # get current directory
		file_path = os.path.join(module_dir, 'serviceAccount.json')
		cred = credentials.Certificate(file_path)
		dfl=firebase_admin.initialize_app(cred)
		opciones.setCredencial(dfl)


	@api_view(['POST', 'GET'])
	def setReserve(request):
		try:
			if request.method == 'POST':
				if(opciones.default_app == None):
					opciones.loadService()
				data=request.data
				code=data['flightCode']
				passengers=data['passengers']
				token=data['token']
				# id_token comes from the client app (shown above)
				decoded_token = auth.verify_id_token(token)
				uid = decoded_token['uid']
				flight=Flight.objects.filter(flightCode=code)
				msg = None;

				if len(flight) > 0:
					passengers2 = flight[0].passengers
					resta= passengers2 - passengers
					if resta >= 0:
						msg='R'
						flight[0].passengers=passengers
						serializer=FlightSerializer(flight, many=True)
						opciones.setConfigDatabase()
						opciones.setDataBase()
						obj=opciones.getDataBase().child("users").child(uid).child("vuelos").get()

						if obj != None:
							print("-----------------entro------------------")
							arregloJson=obj.val()
							fecha=flight[0].date
							fechaStr="%H:%M %d-%m-%Y"
							cadena=fecha.strftime(fechaStr)
							nuevaReserva={
								"flightCode": code,
								"origin": flight[0].origin,
								"destination": flight[0].destination,
								"price": flight[0].price,
								"currency": "COP",
								"date": cadena,
								"passengers": passengers
							}
							arregloJson.append(nuevaReserva)
						else:
							opciones.getDataBase().child("users").child(uid).child("vuelos")
							arregloJson=None
							fecha=flight[0].date
							fechaStr="%H:%M %d-%m-%Y"
							cadena=fecha.strftime(fechaStr)
							nuevaReserva={
								"flightCode": code,
								"origin": flight[0].origin,
								"destination": flight[0].destination,
								"price": flight[0].price,
								"currency": "COP",
								"date": cadena,
								"passengers": passengers
							}
							arregloJson.append(nuevaReserva)
						opciones.getDataBase().child("users").child(uid).child("vuelos").set(arregloJson)
						Flight.objects.filter(flightCode=code).update(passengers=resta)
					else:
						msg= 'I'
				else:
					msg = 'NF'
				return Response(data={"message":msg})
			elif request.method == 'GET' :
				return Response(data={"msg":"se hizo una petición get ."})
		except ValueError:
			return Response(data={"msg":"El token ingresado no es válido, ingrese uno correcto"})


	@api_view(['GET'])
	def getReserves(request, token):
		try:
			if request.method == 'GET':
				if(opciones.default_app == None):
					opciones.loadService()
				# id_token comes from the client app (shown above)
				decoded_token = auth.verify_id_token(token)
				uid = decoded_token['uid']
				opciones.setConfigDatabase()
				opciones.setDataBase()
				obj=opciones.getDataBase().child("users").child(uid).child("vuelos").get()
				arregloJson=obj.val()
				return Response(data={"airline":{"code":"2215","name":"TOPA", "thumbnail":"http://shmector.com/_ph/12/221844079.png"}, "results": arregloJson})
		except ValueError:
			return Response(data={"msg":"El token ingresado no es válido, ingrese uno correcto"})

@api_view(['POST','GET'])
def allFlights(request):
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
