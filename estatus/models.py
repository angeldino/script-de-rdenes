from django.db import models
from django.utils import timezone

class CreateUser(models.Model):
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.user

class CreateClient(models.Model):
    cliente_id = models.CharField(max_length=10, blank=False, null=False, primary_key=True)
    cliente_nombre = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.cliente_nombre

class CreateOrder(models.Model):
    id = models.CharField(max_length=8, null=False, blank=False, primary_key = True)
    cliente = models.ForeignKey(CreateClient, on_delete=models.CASCADE, blank=True, null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    sucursal = models.CharField(max_length=2, default="JZ", blank=False, null=False)
    solicitada_por = models.CharField(max_length=15, default="", blank=True, null=True)
    tipo_orden = models.CharField(max_length=3, default="NAL", blank=False, null=False)
    tipo_carga= models.CharField(max_length=2, default="SE", blank=False, null=False)
    tipo_contenido = models.CharField(max_length=2, default="CA", blank=False, null=False)
    servicio = models.CharField(max_length=4, default="NORM", blank=False, null=False)
    equipo_adicional = models.CharField(max_length=20, blank=True, null=True)
    observaciones = models.CharField(max_length=200, blank=True, null=True)
    fecha_carga = models.DateTimeField(default=timezone.now)
    fecha_salida = models.DateTimeField(default=timezone.now)
    fecha_entrega = models.DateTimeField(default=timezone.now)
    fecha_previo = models.DateField(default=timezone.now)
    sucursal_rol = models.CharField(max_length=2, default="JZ", blank=False, null=False)
    ruta = models.CharField(max_length=2, default="RL", blank=False, null=False)

    def __str__(self):
        return self.id
    
