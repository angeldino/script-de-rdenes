from django.db import models
from django.utils import timezone

class NewTrip(models.Model):
    orden = models.CharField(max_length=255, default="Colocar orden", blank=True, null=True)
    carro = models.CharField(max_length=6, default="", blank=True, null=True)
    remolque = models.CharField(max_length=10, default="", blank=True, null=True)
    origen = models.CharField(max_length=255, default="", blank=True, null=True)
    destination = models.CharField(max_length=255, default="", blank=True, null=True)
    distance = models.CharField(max_length=255, default="", blank=True, null=True)

    def __str__(self):
        return self.order
    
class Lugares(models.Model):
    nombre = models.CharField(max_length=255, default="", blank=True, null=True)
    posicion = models.CharField(max_length=255, default="", blank=True, null=True)

    def __str__(self):
        return self.nombre