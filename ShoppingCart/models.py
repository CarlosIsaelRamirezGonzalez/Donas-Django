from django.db import models
from Inventory.models import Donut
from django.contrib.auth.models import User


# Pedidos -> dirección, cantidad, fk_donas
# Carrito de compras -> fk_usuario, fk_dona, quantity, bill



# Falta poner la ganancia de la tienda de donas

# Set status in Order, like Delivered, In travell, or Dont Delivered
# Replace Delivered 


class Order(models.Model):
    
    class Status(models.TextChoices):
        PROCESS = 'PR', 'Process'
        SENT = 'ST', 'Sent'
        DELIVERED = 'DV', 'Delivered'
        
    address = models.CharField(max_length=350)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.PROCESS)
    user = models.ForeignKey(User, 
                             on_delete=models.CASCADE,
                             related_name='orders',
                             null=True) # user.orders
    donut = models.ForeignKey(Donut,   
                              on_delete=models.CASCADE,
                              related_name='orders') # donut.orders
    
    def __str__(self):
        return self.address
    
class ShoppingCart(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='shopping_cart') # user.shopping_cart
    donut = models.ForeignKey(Donut, 
                              on_delete=models.CASCADE,
                              related_name='shopping_cart') # donut.shopping_cart
    quantity = models.PositiveIntegerField()
    suggestion = models.CharField(max_length=450, null=True)
    bill = models.DecimalField(max_digits=5, decimal_places=2)
    ordered = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.bill
    
