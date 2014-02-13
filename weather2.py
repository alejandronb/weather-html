#coding: utf-8
import requests
import json

direccion = "http://api.openweathermap.org/data/2.5/weather?" #q=London,uk
ciudades = {"1":"Almería","2":"Cádiz","3":"Córdoba","4":"Granada","5":"Huelva","6":"Jaén","7":"Málaga","8":"Sevilla"}

def cardinalidad(direccion):
#Fallo en la funcion
	"Función que transforma los grados en cardinalidades"
	for grado in str(direccion):
		if direccion >= 337.5 and direccion < 22.5:
			return N
		if direccion >= 22.5 and direccion < 67.5:
			return NE
		if direccion >= 67.5 and direccion < 112.5:
			return E
		if direccion >= 112.5 and direccion < 157.5:
			return SE
		if direccion >= 157.5 and direccion < 202.5:
			return S
		if direccion >= 202.5 and direccion < 247.5:
			return SO
		if direccion >= 247.5 and direccion < 292.5:
			return O
		if direccion >= 292.5 and direccion < 337.5:
			return NO


print """1. Almería
2. Cádiz
3. Córdoba
4. Granada
5. Huelva
6. Jaén
7. Málaga
8. Sevilla"""


consulta = raw_input("Introduce el número de la ciudad a consultar: ")

final = "%sq=%s,spain" % (direccion,ciudades[consulta]) #Esto construye la dirección de la API completa
peticion = requests.get(final)
json = json.loads(peticion.text)
tempmax = json["main"]["temp_max"]
tempmin = json["main"]["temp_min"]
viento = json["wind"]["speed"]
direccion = json["wind"]["deg"]
maxima = round(tempmax - 273,1)
minima = round(tempmin - 273,1)
vientokm = round(viento*1.61)

print "La temperatura maxima de %s es %s ºC y la mínima %s ºC y el viento va a %s km/h y su dirección es %s" % (ciudades[consulta],maxima,minima,vientokm,cardinalidad(direccion))
