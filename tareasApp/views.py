from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

lista_personas = [
    ['INFORME TRIMESTRAL','Revisar el informe trimestral de ventas.','24-01-2024','EN PROGRESO','Ana Lopez'],
    ['SITIO WEB','Actualizar contenido y corregir errores.','25-02-2024','EN PROGRESO','Frank Rojas'],
    ['INVESTIGACIÓN','Realizar un estudio de mercado.','13-03-2024','EN PROGRESO','Carla Accostupa'],
]

# Create your views here.
def index(request):
    return render(request,'index.html',{
        'lista_personas':lista_personas
    })

def nuevaTarea(request):
    if request.method == 'POST':
        print(request.POST)
        nombre = request.POST.get('nombre')
        descripción = request.POST.get('descripcion')
        fechaFin = request.POST.get('fecha')
        responsable = request.POST.get('responsable')
        print(nombre)
        print(descripción)
        print(fechaFin)
        print(responsable)
        lista_personas.append([nombre,descripción,fechaFin,'EN PROGRESO',responsable])
        return HttpResponseRedirect(reverse('tareasApp:index'))
    return render(request,'nuevaTarea.html')