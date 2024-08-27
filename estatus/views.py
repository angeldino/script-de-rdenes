from django.shortcuts import render, redirect
from django.utils import timezone
#from .models import CreateOrder, CreateClient  # Reemplaza 'TuModelo' por el nombre de tu modelo
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def register(request):
    return render(request, "index.html")

def create_new_trip(request):
    if request.method == 'POST':
        order = request.POST.get('order')
        trailer = request.POST.get('trailer')
        remolque = request.POST.get('remolque')
        posicion = request.POST.get('posicion')
        destino = request.POST.get('destino')
        distancia = request.POST.get('distancia')
        tiempo_estimado = request.POST.get('tiempo_estimado')

        # Crear una nueva instancia de NewTrip y guardar los datos
        new_trip = NewTrip(
            order=order,
            trailer=trailer,
            remolque=remolque,
            posicion=posicion,
            destino=destino,
            distancia=distancia,
            tiempo_estimado=tiempo_estimado
        )
        new_trip.save()

        return redirect('home')  # Redirige a una página de éxito después de guardar

    return render(request, 'index.html')