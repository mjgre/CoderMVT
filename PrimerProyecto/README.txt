Mi proyecto cuenta con:

Vistas
Formularios
3 Modelos
Templates de inicio, carga de datos y busqueda de datos



Pasos para utilizar el proyecto:
1- Chequear que tengas python instalado  

		En windows tiene que abrir una terminal cmd o powershell.
		PS C:\> python --version
		Python 3.X.X 

		En Linux/Mac tiene que abrir una terminal bash
		$ python --version
		Python 3.X.X 

2- Instalar Django
		En una terminal cmd o powershell desde windows:
		C:\> pip install django
		
		Linux/Mac:
		$ pip install django

3-Instalar django bootstrap v5
		Windows:
		C:\> pip install django-bootstrap-v5

		Linux/Mac:
		$ pip install django-bootstrap-v5

4-Los siguinetes comandos son analogos en Mac/Linux/Windows:

		cd mi-primer-mvt
		python manage.py migrate

		La consola mostrara las migraciones de la base de datos que se realizaron.
		Luego arrancamos el servidor web:

		python manage.py runserver

5-Ingresamos a http://127.0.0.1:8000/familia

Una ves dentro de la pantalla principal, podemos navegar por el proyecto a traves de la barra de navegacion y las 3 opciones 
Miembros de la familia, evento y tareas.
Dentro de cada modulo tenemos botones de carga para ingresar familiares, tareas o asistentes al evento depende cada caso. 
Una vez cargado algun individuo, nos aparecera el boton de BORRAR que nos eliminara los datos del renglon seleccionado. 
Por ultimo, el modulo Miembros de la familia, tiene un boton BUSCAR que nos servira en caso de tener muchos parientes cargados para buscarlos por su NOMBRE.


