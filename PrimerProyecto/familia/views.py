from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.shortcuts import render
from familia.forms import BuscarPersonasForm, PersonaForm
from familia.forms import EventoForm
from familia.forms import TareasForm

from familia.models import Evento, Persona, Tareas

def index(request):
    personas = Persona.objects.all()
    template = loader.get_template('familia/index.html')
    context = {
        'personas': personas,
    }
    return HttpResponse(template.render(context, request))


def agregar(request):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue cargada con éxito
    '''

    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            edad = form.cleaned_data['edad']
            email = form.cleaned_data['email']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            Persona(nombre=nombre, apellido=apellido, edad=edad, email=email, fecha_nacimiento=fecha_nacimiento).save()

            return HttpResponseRedirect("/familia/")
    elif request.method == "GET":
        form = PersonaForm()
    else:
        return HttpResponseBadRequest("Error no conozco ese metodo para esta request")

    
    return render(request, 'familia/form_carga.html', {'form': form})


def borrar(request, identificador):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue eliminada con éxito        
    '''
    if request.method == "GET":
        persona = Persona.objects.filter(id=int(identificador)).first()
        if persona:
            persona.delete()
        return HttpResponseRedirect("/familia/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


def actualizar(request, identificador):
    '''
    TODO: implementar una vista para actualización
    '''
    pass

def indexEv(request):
    evento = Evento.objects.all()
    template = loader.get_template('familia/index_evento.html')
    context = {
        'evento': evento,
    }
    return HttpResponse(template.render(context, request))


def indexTa(request):
    tareas = Tareas.objects.all()
    template = loader.get_template('familia/index_tareas.html')
    context = {
        'tareas': tareas,
    }
    return HttpResponse(template.render(context, request))

def evento(request):
    '''
    TODO: agregar un mensaje en el template form_cargaEvento.html que avise al usuario que 
    la persona fue cargada con éxito
    '''

    if request.method == "POST":
        form = EventoForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            asistencia = form.cleaned_data['asistencia']
            comida = form.cleaned_data['comida']
            bebida = form.cleaned_data['bebida']
            Evento(nombre=nombre, apellido=apellido, asistencia=asistencia, comida=comida, bebida=bebida).save()

            return HttpResponseRedirect("/familia/evento/")
    elif request.method == "GET":
        form = EventoForm()
    else:
        return HttpResponseBadRequest("Error no conozco ese metodo para esta request")

    
    return render(request, 'familia/form_cargaEvento.html', {'form': form})

def tareas(request):
    '''
    TODO: agregar un mensaje en el template form_cargaTareas.html que avise al usuario que 
    la persona fue cargada con éxito
    '''

    if request.method == "POST":
        form = TareasForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            tarea = form.cleaned_data['tarea']
            horario = form.cleaned_data['horario']
            duracion = form.cleaned_data['duracion']
            Tareas(nombre=nombre, apellido=apellido, tarea=tarea, horario=horario, duracion=duracion).save()

            return HttpResponseRedirect("/familia/tareas/")
    elif request.method == "GET":
        form = TareasForm()
    else:
        return HttpResponseBadRequest("Error no conozco ese metodo para esta request")

    
    return render(request, 'familia/form_cargaTareas.html', {'form': form})

def borrarEv(request, identificador):
    '''
    TODO: agregar un mensaje en el template form_evento.html que avise al usuario que 
    la persona fue eliminada con éxito        
    '''
    if request.method == "GET":
        evento = Evento.objects.filter(id=int(identificador)).first()
        if evento:
            evento.delete()
        return HttpResponseRedirect("/familia/evento/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

        
def borrarTa(request, identificador):
    '''
    TODO: agregar un mensaje en el template form_tareas.html que avise al usuario que 
    la persona fue eliminada con éxito        
    '''
    if request.method == "GET":
        tareas = Tareas.objects.filter(id=int(identificador)).first()
        if tareas:
            tareas.delete()
        return HttpResponseRedirect("/familia/tareas/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


def buscar(request):
    
    if request.GET.get("palabra_a_buscar") and request.method == "GET":
        form_busqueda = BuscarPersonasForm(request.GET)
        if form_busqueda.is_valid():
            personas = Persona.objects.filter(nombre__icontains=request.GET.get("palabra_a_buscar"))
            return  render(request, 'familia/index.html', {"personas": personas, "resultados_busqueda":True})

    elif request.method == "GET":
        form_busqueda = BuscarPersonasForm()
        return render(request, 'familia/form_busqueda.html', {"form_busqueda": form_busqueda})