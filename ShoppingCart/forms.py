from django import forms
from .models import ShoppingCart, Order


class ShoppingForm(forms.ModelForm):
    class Meta:
        model = ShoppingCart
        fields = ['quantity', 'suggestion']
    
class AddressForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address']