from django.http import HttpResponse

def mostrar_bienvenida(request):
    return HttpResponse("¡Bienvenidos a mi primera app Django, Vicen!")
