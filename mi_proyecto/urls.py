
from django.urls import path
from bienvenida.views import mostrar_bienvenida

urlpatterns = [
    path('inicio/', mostrar_bienvenida, name='mostrar_bienvenida'),
]