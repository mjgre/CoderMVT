from django.urls import path
from familia import views


urlpatterns = [
    path('', views.index, name="index"),
    path('agregar/', views.agregar, name="agregar"),
    path('borrar/<identificador>', views.borrar, name="borrar"),
    path('tareas/borrar-tarea/<identificador>', views.borrarTa, name="borrar-tarea"),
    path('evento/borrar-evento/<identificador>', views.borrarEv, name="borrar-evento"),
    path('evento/', views.indexEv, name="evento"),
    path('tareas/', views.indexTa, name="tareas"),
    path('eventocarga/', views.evento, name="eventocarga"),
    path('tareascarga/', views.tareas, name="tareascarga"),
    path('buscar/', views.buscar, name="buscar"),
]