from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from ShoppingCart.models import ShoppingCart
from django.views.generic import ListView, FormView
from django.views.generic.edit import FormMixin

from .models import Donut


class HomeView(ListView):
    queryset = Donut.objects.all()
    context_object_name = 'donuts'
    paginate_by = 10
    template_name = 'inventory/home.html'

    def get_context_data(self, **kwargs):
        # Llama al contexto base para obtener los datos predeterminados
        context = super().get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            cart_shopping_number = ShoppingCart.objects.filter(user=self.request.user).count()
        else:
            cart_shopping_number = 0
        
        context['cart_shopping_number'] = cart_shopping_number
        
        return context
    
    
def terms_and_conditions(request):
    return render(request, 'inventory/terms_and_conditions.html')