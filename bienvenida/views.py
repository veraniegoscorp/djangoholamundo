from django.http import HttpResponse
from .models import producto
from django.shortcuts import render



def mostrar_bienvenida(request):
    return HttpResponse("oal shavo")


def lista_productos(request):
    productos = producto.objects.all()
    return render(request, 'productos/lista.html', {'productos':productos})