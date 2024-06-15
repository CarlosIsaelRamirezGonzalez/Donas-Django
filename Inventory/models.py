from django.db import models

# Donas -> nombre, descripción, precio, cantidad
class Donut(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    nutritional_information = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField() # Quantity or Stock?
    
    class Meta:
        ordering = ['price']
    
    def __str__(self):
        return self.name
