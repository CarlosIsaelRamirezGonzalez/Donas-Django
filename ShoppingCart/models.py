from django.db import models
from Inventory.models import Donut
from django.contrib.auth.models import User


# Pedidos -> dirección, cantidad, fk_donas
# Carrito de compras -> fk_usuario, fk_dona, quantity, bill

class Order(models.Model):
    address = models.CharField(max_length=350)
    quantity = models.PositiveIntegerField()
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
    bill = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.bill
    
