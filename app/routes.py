import requests
import json

from flask import request
from app import app

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

jwt = JWTManager(app)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/agent', methods=['POST'])
def obtainToken():

	nombre = request.json.get('nombre', None)
	clave = request.json.get('clave', None)

	datos = requests.get(('https://617dc58c1eadc500171365fd.mockapi.io/agent?nombre={}').format(nombre)).json()

	print(datos, flush=True)

	for usuario in datos:

		if(nombre == usuario['nombre'] and clave == usuario['clave']):
			token = create_access_token(identity=nombre)

			return json.dumps({
					"nombre": nombre,
					"token": token
			})

	return 'Usuario incorrecto'

#Metodo para enviar Issues
@app.route('/issue', methods=['POST'])
@jwt_required()
def postIssues():

	#Datos iniciales
	fecha = ""
	titulo = ""
	descripcion = ""
	agente = get_jwt_identity()

	print(agente, flush=True)

	#try:
	datos = request.get_json()
	#except TypeError:
	#	return ('El formato de los datos debe ser JSON') #En caso de que los datos no se envien como json

	try:
		fecha = datos['fecha']
		titulo = datos['titulo']
		descripcion = datos['descripcion']
		agente = get_jwt_identity()
	except KeyError as err:
		return (('Falta uno de los valores: {}').format(err)) #Retorna como error el nombre del primer atributo que falta
	except TypeError as err:
		return (('El tipo no es correcto: {}').format(err)) #Retorna como error el tipo

	if(fecha != "" and fecha is not None and
  	titulo != "" and titulo is not None and
  	descripcion != "" and descripcion is not None and
  	agente != "" and agente is not None): #Verifica que existan los datos

		contenido = {
			"fecha": fecha,
			"titulo": titulo,
			"descripcion": descripcion,
		 	"agente": agente
		}

		print(contenido)

		requests.post('https://617dc58c1eadc500171365fd.mockapi.io/issue', json=contenido) #Envia los datos a MockAPI
		return "El issue {} ha sido ingresado correctamente".format(titulo)
	else:
		return "Uno de los atributos no ha sido ingresado correctamente"



#Metodo para seleccionar los distintos tipos de issues.
#Existen 3 tipos de respuestas, en base a los atributos enviados.
#agente: Devuelve los issues que tengan el nombre de agente correspondiente.
#fecha: Devuelve los issues que tengan la fecha correspondiente.
#vacio: En caso de no enviar atributos se devuelven todos los issues.
#En caso de tener nombre y fecha se devuelve la misma respuesta que solo nombre.
@app.route('/issues', methods=['GET'])
def getIssues():
		agente = request.args.get('agente', default="", type=str)
		fecha = request.args.get('fecha', default="", type=str)
		if agente != "":
			lista = json.loads(requests.get(('https://617dc58c1eadc500171365fd.mockapi.io/issue?agente={}').format(agente)).text)
			respuesta = []

			for issue in lista:
				if agente == issue['agente']:
					respuesta.append(issue)

			return {"contenido": respuesta }

		elif fecha != "":
			#print (fecha, flush=True)
			#print (('https://617dc58c1eadc500171365fd.mockapi.io/issue?fecha={}').format(fecha), flush=True)
			return {"contenido": json.loads(requests.get(('https://617dc58c1eadc500171365fd.mockapi.io/issue?fecha={}').format(fecha)).text)}
		else:
			return {"contenido": json.loads(requests.get('https://617dc58c1eadc500171365fd.mockapi.io/issue').text)}

