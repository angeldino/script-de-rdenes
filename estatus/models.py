from django.db import models
from django.utils import timezone

class NewTrip(models.Model):
    order = models.CharField(max_length=255, default="Colocar orden", blank=True, null=True)
    trailer = models.CharField(max_length=6, default="", blank=True, null=True)
    remolque = models.CharField(max_length=10, default="", blank=True, null=True)
    posicion = models.CharField(max_length=255, default="", blank=True, null=True)
    destino = models.CharField(max_length=255, default="", blank=True, null=True)
    distancia = models.CharField(max_length=255, default="", blank=True, null=True)
    tiempo_estimado = models.CharField(max_length=255, default="", blank=True, null=True)

    def __str__(self):
        return self.order
    
class Lugares(models.Model):
    nombre = models.CharField(max_length=255, default="", blank=True, null=True)
    posicion = models.CharField(max_length=255, default="", blank=True, null=True)

    def __str__(self):
        return self.nombre