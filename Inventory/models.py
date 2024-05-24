from django.db import models

# Donas -> nombre, descripción, precio, cantidad
class Donut(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=2, decimal_places=2)
    quantity = models.PositiveIntegerField()
    
    class Meta:
        ordering = ['price']
    
    def __str__(self):
        return self.name
