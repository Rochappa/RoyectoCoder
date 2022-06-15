import email
from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Estudiante

# Create your views here.

def curso(self):

    curso = Curso(nombre = "Web", camada = '1234')

    curso.save()

    documento = f'El curso es: {curso.nombre}, la camada es: {curso.camada}'

    return HttpResponse(documento)

def estudiantes(self):
    
    estudiante2 = Estudiante(nombre= "Luis", apellido = "Alvarez", email = "hola@gmail.com")
    
    estudiante2.save()
    
    documento = f"El estudiante es : {estudiante2.nombre}\n el apellido es: {estudiante2.apellido}\n el mail es: {estudiante2.email}"
    
    return HttpResponse(documento)


