from django.db import models
from django.contrib.auth.models import User

# Donas -> nombre, descripción, precio, cantidad
class Donut(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    nutritional_information = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date_expirity = models.DateField(null=True, blank=True)
    quantity = models.PositiveIntegerField() 
    
    class Meta:
        ordering = ['price']
    
    def __str__(self):
        return self.name
    
class Profits(models.Model):
    profit =  models.DecimalField(max_digits=999, decimal_places=2)
    user = models.ForeignKey(User, 
                             on_delete=models.CASCADE,
                             related_name='profits',
                             null=True) # user.orders
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        ordering = ['user']
    
        
    def __str__(self):
        return str(self.profit) 