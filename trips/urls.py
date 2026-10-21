from django.urls import path   # Función path para definir rutas
from . import views            # importamos las vistas de esta app

app_name = 'trips'  # Espacio de nombres para usar rutas como trips:home



urlpatterns = [ 
               path('', views.home, name='home'), # Ruta raíz de la pp: llama a la vista home

]