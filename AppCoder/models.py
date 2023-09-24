from django.db import models

# Clases

class Cafe_Caliente(models.Model):
    nombre = models.CharField(max_length=20)
    tamaño = models.CharField(max_length=10)
    precio = models.FloatField()
    disponibilidad = models.BooleanField()

class Cafe_Frio(models.Model):
    nombre = models.CharField(max_length=20)
    tamaño = models.CharField(max_length=10)
    precio = models.FloatField()
    disponibilidad = models.BooleanField()

class Comida(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.FloatField()
    disponibilidad = models.BooleanField()