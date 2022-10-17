from django.shortcuts import render
from ejemplo.models import Familiar

def index(request):
    return render(request, "ejemplo/saludar.html")

def saludar_a(request, nombre, apellido):
    return render(request, 'ejemplo/saludar.html', {'nombre': nombre, 'apellido': apellido})

def index_dos(request):    
    return render(request, 'ejemplo/numeros.html', {'lista_numeros': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})    

def mostrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})

def imc(request, altura, peso ):
    altura_en_metros = int(altura) / 100
    peso_en_kilos = int(peso) / 100
    imc = peso_en_kilos / (altura_en_metros ** 2)
    return render(request, 'ejemplo/imc.html', {'altura': altura, 'peso': peso, 'imc': imc})

