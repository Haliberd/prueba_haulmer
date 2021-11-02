from flask import Flask


app = Flask(__name__)

#Configuracion JWT
app.config["JWT_SECRET_KEY"] = "prueba_haulmer"  #Clave 'secreta'

from app import routes
