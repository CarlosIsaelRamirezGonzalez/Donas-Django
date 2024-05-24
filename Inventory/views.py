from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, FormView
from django.views.generic.edit import FormMixin

from .models import Donut


class HomeView(ListView):
    queryset = Donut.objects.all()
    context_object_name = 'donuts'
    paginate_by = 10
    template_name = 'inventory/home.html'
    
    
def index(request):
    return render(request, 'inventory/index.html')

def terms_and_conditions(request):
    return render(request, 'inventory/terms_and_conditions.html')