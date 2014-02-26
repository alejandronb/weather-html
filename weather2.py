#coding: utf-8
import requests
import json
from jinja2 import Template
import webbrowser
import os

ciudades = ['Almeria','Cadiz','Cordoba','Granada','Huelva','Jaen','Malaga','Sevilla']
f = open("plantilla.html","r")
salida = open("salida.html","w")
html = ''

def cardinalidad(direccion):
	"Función que transforma los grados en cardinalidades"
	for degree in str(direccion):
		if direccion >= 337.5 and direccion < 22.5:
			return "N"
		elif direccion >= 22.5 and direccion < 67.5:
			return "NE"
		elif direccion >= 67.5 and direccion < 112.5:
			return "E"
		elif direccion >= 112.5 and direccion < 157.5:
			return "SE"
		elif direccion >= 157.5 and direccion < 202.5:
			return "S"
		elif direccion >= 202.5 and direccion < 247.5:
			return "SO"
		elif direccion >= 247.5 and direccion < 292.5:
			return "O"
		elif direccion >= 292.5 and direccion < 337.5:
			return "NO"


for linea in f:
	html += linea


temp_max = []
temp_min = []
viento_km = []
direccion_viento = []


for ciudad in ciudades:
	peticion = requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'%s,spain' % ciudad})
	dicc = json.loads(peticion.text)
	tempmax = dicc["main"]["temp_max"]
	tempmin = dicc["main"]["temp_min"]
	viento = dicc["wind"]["speed"]
	direccion = dicc["wind"]["deg"]
	maxima = round(tempmax - 273,1)
	minima = round(tempmin - 273,1)
	vientokm = round(viento*1.61)
	temp_max.append(maxima)
	temp_min.append(minima)
	viento_km.append(vientokm)
	direccion_viento.append(cardinalidad(direccion))

template = Template(html)
template = template.render(ciudades=ciudades,maxima=temp_max,minima=temp_min,viento=viento_km,direccion=direccion_viento)
web.write(template)
webbrowser.open("salida.html")


