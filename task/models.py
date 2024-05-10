from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Aquí puedes colocar el insert de la dona
    @classmethod
    def insertar_brownie_donut(cls):
        cls.objects.create(nombre="Brownie_Donut", precio=15)
class CarritoItem(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, default='Dirección predeterminada')
    estate = models.CharField(max_length=100, default='Estado predeterminado')
    postalcode = models.CharField(max_length=10, default='00000')
   

    def __str__(self):
        return self.usuario.username  



class Orden(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos = models.CharField(max_length=255, default='Sin productos')  # Almacena los nombres de los productos como una cadena de texto
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Orden {self.id}"



  # Agregar el campo datecompleted


