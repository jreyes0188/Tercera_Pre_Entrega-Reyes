from django.urls import path
from .views import *

urlpatterns = [
    path("inicio/", inicio, name = "Inicio"),
    path("cafe_caliente/", ver_cafe_caliente, name = "VerCafeCaliente"),
    path("cafe_frio/", ver_cafe_frio, name = "VerCafeFrio"),
    path("comida/", ver_comida, name = "VerComida"),
    path("resultado_cafe_caliente/", resultado_cafe_caliente, name = "ResultadoCafeCaliente"),
    path("resultado_cafe_frio/", resultado_cafe_frio, name = "ResultadoCafeFrio"),
    path("resultado_comida/", resultado_comida, name = "ResultadoComida"),
]