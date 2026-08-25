
from django.urls import path
from bienvenida.views import mostrar_bienvenida,lista_productos




urlpatterns = [
    path('inicio/', mostrar_bienvenida, name='mostrar_bienvenida'),
    path('lista_productos/', view=lista_productos, name="lista productos")
]