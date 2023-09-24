from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import *
from .models import *

# Formularios POST

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def ver_cafe_caliente(request):
    if request.method == "POST":
        formulario_1 = Cafe_Caliente_Form(request.POST)
        if formulario_1.is_valid():
            info = formulario_1.cleaned_data
            cafe_caliente = Cafe_Caliente(nombre=info["nombre"], tamaño=info["tamaño"], precio=info["precio"], disponibilidad=info["disponibilidad"])
            cafe_caliente.save()
            return render(request, "AppCoder/inicio.html")
    else:
        formulario_caliente = Cafe_Caliente_Form()
    return render(request, "AppCoder/ver_cafe_caliente.html", {"form_1": formulario_caliente})

def ver_cafe_frio(request):
    if request.method == "POST":
        formulario_2 = Cafe_Frio_Form(request.POST)
        if formulario_2.is_valid():
            info = formulario_2.cleaned_data
            cafe_frio = Cafe_Frio(nombre=info["nombre"], tamaño=info["tamaño"], precio=info["precio"], disponibilidad=info["disponibilidad"])
            cafe_frio.save()
            return render(request, "AppCoder/inicio.html")
    else:
        formulario_frio = Cafe_Frio_Form()
    return render(request, "AppCoder/ver_cafe_frio.html", {"form_2": formulario_frio})

def ver_comida(request):
    if request.method == "POST":
        formulario_3 = Comida_Form(request.POST)
        if formulario_3.is_valid():
            info = formulario_3.cleaned_data
            comida = Comida(nombre=info["nombre"], precio=info["precio"], disponibilidad=info["disponibilidad"])
            comida.save()
            return render(request, "AppCoder/inicio.html")
    else:
        formulario_comida = Comida_Form()
    return render(request, "AppCoder/ver_comida.html", {"form_3": formulario_comida})


# Formulario GET ---> Cafe Caliente

def busqueda_cafe_caliente(request):
    return render(request, "AppCoder/ver_cafe_caliente.html")

def resultado_cafe_caliente(request):
    
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        cafe_calientes = Cafe_Caliente.objects.filter(nombre__iexact = nombre) 
        
        return render(request, "AppCoder/ver_cafe_caliente.html", {"cafe_calientes": cafe_calientes, "nombre": nombre})
    
    else:
        respuesta = "No realizaste la consulta"
    
    return HttpResponse(respuesta)


# Formulario GET ---> Cafe Frio

def busqueda_cafe_frio(request):
    return render(request, "AppCoder/ver_cafe_frio.html")

def resultado_cafe_frio(request):
    
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        cafe_frios = Cafe_Frio.objects.filter(nombre__iexact = nombre) 
        
        return render(request, "AppCoder/ver_cafe_frio.html", {"cafe_frios": cafe_frios, "nombre": nombre})
    
    else:
        respuesta = "No realizaste la consulta"
    
    return HttpResponse(respuesta)


# Formulario GET ---> Comida

def busqueda_comida(request):
    return render(request, "AppCoder/ver_comida.html")

def resultado_comida(request):
    
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        comidas = Comida.objects.filter(nombre__iexact = nombre) 
        
        return render(request, "AppCoder/ver_comida.html", {"comidas": comidas, "nombre": nombre})
    
    else:
        respuesta = "No realizaste la consulta"
    
    return HttpResponse(respuesta)


