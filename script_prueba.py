import requests
from datetime import datetime


nombre_usuario = 'nombre 1' #Nombre de usuario, estos siguen la estructura nombre x, donde x es un numero
clave_usuario = 'clave 1' #Clave de usuario, sigue una estructura similar a nombre_usuario

usuario = {
	"nombre": nombre_usuario,
	"clave": clave_usuario
}

resultado_autentificacion = requests.post('http://localhost:5000/agent', json=usuario).json()

print (resultado_autentificacion)

try:
	token = resultado_autentificacion['token']
	#print (token)
	contenido_issue = {
		"fecha": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
		"titulo": "Prueba",
		"descripcion": "Prueba de insertar un issue",
		"agente": nombre_usuario
	}

	print('Bearer {}'.format(token))

	resultado_crear_issue = requests.post('http://localhost:5000/issue',
		headers={'Authorization': 'Bearer {}'.format(token)}, json=contenido_issue).text
	print (resultado_crear_issue)

except:
	print ('El usuario no existe o su clave es incorrecta')
