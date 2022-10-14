from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar

# Create your views here.

def familiar(request, nombre, edad, fecha_nacimiento):
    
    familiar = Familiar(nombre=nombre, edad=edad, fecha_nacimiento=fecha_nacimiento)
    familiar.save()
    
    return HttpResponse(f""" <p>Familiar agregado </p>""")

def lista_familiares(request):
    
    lista = Familiar.objects.all()    
    return render(request, 'index.html', {"lista" : lista})
    