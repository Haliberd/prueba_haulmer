# Prueba Haulmer
Dentro de este archivo README se describirán los pasos necesarios para el correcto funcionamiento de esta prueba.

1. Descargar el repositorio git.
2. Dentro de la carpeta del repositorio, ejecutar la siguiente linea **docker build -f Dockerfile -t prueba_haulmer:latest .**. Dicha linea sirve para crear una imagen de Docker, de la cual crearemos el contenedor en el cual el servidor se encuentra almacenado.
3. Ejecutar la siguiente linea **docker run -d -p 5000:5000 prueba_haulmer:latest**. Dicha linea sirve para crear y correr un contenedor con los datos de la imagen creada anteriormente. Cabe destacar de que la frase 5000:5000 señala los puertos que va a ocupar el servidor, tanto afuera del contenedor como dentro del contenedor respectivamente. Si es que el puerto 5000 se encuentra ocupado por alguna otra aplicación entonces puede modificar dicha linea para que apunte hacía otro puerto, por ejemplo 6791:5000, siempre y cuando se mantenga el puerto 5000 en la ultima parte, dado a que el servidor dentro del contenedor se encuentra corriendo en dicho puerto.
4. Finalmente, podemos revisar rapidamente si es que el contendor se encuentra operando correctamente si es que probamos con la ruta localhost:(puerto asignado)/issues, la cual debería de devolver el listado de issues.

Cabe destacar de que es necesario tener Docker para poder ejecutar las instrucciones anteriores correctamente.



5. Una vez encendido el servidor usar Postman u otra herramienta similar para usar el metodo POST 'ruta':'puerto_abierto'/agent, ejemplo localhost:5000/agent. Dicha ruta devuelve un token, el cual es necesario para la ruta /issue.
  * Dicha ruta requiere un nombre y una clave de agente.
    * No existe una ruta definida dentro de la API del servidor para crear agentes. Se puede crear un agente si es que se toma la ruta definida dentro del programa y en vez de, por ejemplo, apuntar a <ruta_de_mockapi>/agent, usando POST. En dicho caso, deben de ser definidos los atributos nombre y clave dentro de body, preferiblemente en formato JSON.
    * Los agentes siguen la siguiente estructura:
      * nombre x
      * clave x
    * Los token tienen un periodo de expiración.

6. Una vez obtenido el token, este debe de ser ingresado en el apartado de autentificación, con la etiqueta Bearer. Tomando esto en cuenta ahora se puede acceder a la ruta /issue. 
  * Dicha ruta toma los siguientes paramentros:
    * fecha (tipo DATE)
    * titulo
    * descripcion
    * agente (nombre de agente responsable de ingresar dicho issue.
  * Para ingresar un issue solo es necesario ingresar los primeros 3 atributos en formato JSON.

7. Finalmente, la ultima ruta /issues entrega una lista de issues según los parametros indicados en el header.
 * Si se ingresa /issues?agente entonces se obtienen todos los issues creador por dicho agente. Es necesario ingresar el nombre del agente.
 * Si se ingresa /issues?fecha entonces se obtienen todos los issues creados en una cierta fecha. Es necesario ingresar la fecha.
 * Si se ingresa /issues entonces se obtienen todos los issues.

El script script_prueba.py se ejecuta de forma estandar, es decir:
* py script_prueba.py

Dicho script ingresa como usuario "nombre 1", obtiene un token y luego usa dicho token para crear un issue. Es posible modificar los parametros del issue sin problema (excepto por fecha), sin embargo, modificar el nombre y la clave del usuario puede generar conflictos, se recomienda manejar dicho usuario de tal forma que tanto el numero de nombre como clave sea el mismo y estos se encuentren dentro del margen [1, 10].


   
    
