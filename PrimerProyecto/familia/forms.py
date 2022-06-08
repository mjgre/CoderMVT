from unittest.util import _MAX_LENGTH
from django import forms

class PersonaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    edad = forms.IntegerField(label="Edad")
    email = forms.EmailField(label="Email")
    # input_format hace que se pueda ingresar la fecha con el formato latino, dia/mes/año
    fecha_nacimiento = forms.DateField(label="fecha_nacimiento", input_formats=["%d/%m/%Y"],
    #widget es para poder agregar un tip para que el usuario sepa como ingresar la fecha
    widget=forms.TextInput(attrs={'placeholder': '30/12/1995'}))

class EventoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    asistencia = forms.CharField(label="Asistencia")
    comida = forms.CharField(label="comida")
    bebida = forms.CharField (label="bebida")

class TareasForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    tarea = forms.CharField(label="Tarea")
    horario = forms.IntegerField(label="Horario")
    duracion = forms.IntegerField(label="Duracion de la tarea")


class BuscarPersonasForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")