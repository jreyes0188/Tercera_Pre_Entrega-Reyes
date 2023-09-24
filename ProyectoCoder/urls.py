from django.contrib import admin
from django.urls import path, include
from AppCoder.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path("App/", include("AppCoder.urls")), # Le pasamos las urls que se encuentran en AppCoder
    path("", inicio) # Para que la url http://127.0.0.1:8000/ sea la pagina de inicio
]
