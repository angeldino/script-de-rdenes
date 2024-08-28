from django.views import View
from django.shortcuts import render, redirect
from django.http import JsonResponse
#from .models import CreateOrder, CreateClient  # Reemplaza 'TuModelo' por el nombre de tu modelo
from django.contrib import messages
from django.utils.decorators import method_decorator
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def register(request):
    return render(request, "index.html")

@csrf_exempt
def calculate_distance(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            origin = data.get('origin')
            destination = data.get('destination')
            orden = data.get('orden')
            carro = data.get('carro')
            remolque = data.get('remolque')
            distance = data.get('distance')

            # Guarda en la base de datos
            location_distance = NewTrip(
                origin=origin,
                destination=destination,
                distance=distance,
                orden=orden,
                carro=carro,
                remolque=remolque
            )
            location_distance.save()

            return JsonResponse({'status': 'success'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)