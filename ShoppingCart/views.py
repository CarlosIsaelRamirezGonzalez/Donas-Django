from django.shortcuts import render,  get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from Inventory.models import Donut
from django.urls import reverse_lazy
from django.views.generic import FormView
from .models import ShoppingCart
from .forms import ShoppingForm


@method_decorator(login_required, name='dispatch')
class ShopingFormView(FormView):
    template_name = 'shopping'
    form_class = ShoppingForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        quantity = form.cleaned_data['quantity']
        suggestion = form.cleaned_data['suggestion']
        user = self.request.user
        donut_id = self.kwargs['donut_id']
        donut = get_object_or_404(Donut, id=donut_id)
        suggestion = form.cleaned_data['suggestion']
        bill = donut.price * quantity
        
        ShoppingCart.objects.create(
            user=user,
            donut=donut,
            quantity=quantity,
            suggestion=suggestion, 
            bill=bill
        )
        
        return redirect(self.success_url)
        
    def form_invalid(self, form):
        error_message = "The data provided is not valid."
        messages.error(self.request, error_message)
        return self.render_to_response(self.get_context_data(form=form))
    


    