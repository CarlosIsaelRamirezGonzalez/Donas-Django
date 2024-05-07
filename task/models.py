from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True) #permite que el campo este en blanco
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class CarritoItem(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, default='Dirección predeterminada')
    estate = models.CharField(max_length=100, default='Estado predeterminado')
    postalcode = models.CharField(max_length=10, default='00000')
    debito = models.CharField(max_length=16, default='0000-0000-0000-0000')  # Valor predeterminado # Campo para el número de tarjeta de débito
    cvc = models.CharField(max_length=4,default='0000')  # Campo para el CVC de la tarjeta de débito
    due_date = models.CharField(max_length=10, default="31/12/2025")  # Campo para la fecha de vencimiento de la tarjeta de débito

    def __str__(self):
        return self.usuario.username  



class Orden(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField(CarritoItem)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)  # Agregar el campo datecompleted

    def __str__(self):
        return f"Orden {self.id}"

