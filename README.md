# Prueba Haulmer
Dentro de este archivo README se describirán los pasos necesarios para el correcto funcionamiento de esta prueba.

1. Descargar el repositorio git.
2. Ejecutar la siguiente linea **docker build -f Dockerfile -t prueba_haulmer:latest .**. Dicha linea sirve para crear una imagen de Docker, de la cual crearemos el contenedor en el cual el servidor se encuentra almacenado.
3. Ejecutar la siguiente linea **docker run -d -p 5000:5000 prueba_haulmer:latest**. Dicha linea sirve para crear y correr un contenedor con los datos de la imagen creada anteriormente. Cabe destacar de que la frase 5000:5000 señala los puertos que va a ocupar el servidor, tanto afuera del contenedor como dentro del contenedor respectivamente. Si es que el puerto 5000 se encuentra ocupado por alguna otra aplicación entonces puede modificar dicha linea para que apunte hacía otro puerto, por ejemplo 6791:5000, siempre y cuando se mantenga el puerto 5000 en la ultima parte, dado a que el servidor dentro del contenedor se encuentra corriendo en dicho puerto.
4. Finalmente, podemos revisar rapidamente si es que el contendor se encuentra operando correctamente si es que probamos con la ruta localhost:(puerto asignado)/issues, la cual debería de devolver el listado de issues.
