from concurrent.futures.process import _MAX_WINDOWS_WORKERS
from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    asistencia = models.CharField(max_length=100)
    comida = models.CharField(max_length=100)
    bebida = models.CharField(max_length=100)


class Tareas(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    tarea = models.CharField(max_length=100)
    horario = models.IntegerField()
    duracion = models.IntegerField()
    