from django import forms

class Cafe_Caliente_Form(forms.Form):
    nombre = forms.CharField(max_length=20)
    tamaño = forms.CharField(max_length=10)
    precio = forms.FloatField()
    disponibilidad = forms.BooleanField()
    
class Cafe_Frio_Form(forms.Form):
    nombre = forms.CharField(max_length=20)
    tamaño = forms.CharField(max_length=10)
    precio = forms.FloatField()
    disponibilidad = forms.BooleanField()


class Comida_Form(forms.Form):
    nombre = forms.CharField(max_length=20)
    precio = forms.FloatField()
    disponibilidad = forms.BooleanField()