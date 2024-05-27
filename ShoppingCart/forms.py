from django import forms
from .models import ShoppingCart


class ShoppingForm(forms.ModelForm):
    class Meta:
        model = ShoppingCart
        fields = ['quantity', 'suggestion']
    