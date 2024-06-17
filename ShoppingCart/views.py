from django.shortcuts import render,  get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views import View
from django.http import HttpResponseBadRequest
from Inventory.models import Donut
from django.urls import reverse_lazy
from django.views.generic import FormView
from .models import ShoppingCart
from .forms import ShoppingForm

@method_decorator(login_required, name='dispatch')
class ShoppingFormView(View):
    template_name = 'shopping_cart/shopping.html'
    success_url = reverse_lazy('inventory:home')

    def get(self, request, donut_id):
        form = ShoppingForm()
        donut = get_object_or_404(Donut, id=donut_id)
        return render(request, self.template_name, {'form': form, 'donut': donut})
    
    def post(self, request, donut_id):
        form = ShoppingForm(request.POST)
        donut = get_object_or_404(Donut, id=donut_id)
        
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            suggestion = form.cleaned_data['suggestion']
            user = request.user
            bill = donut.price * quantity

            ShoppingCart.objects.create( # When use create the instance of the class is automatically saved in thed database
                user=user,
                donut=donut,
                quantity=quantity,
                suggestion=suggestion, 
                bill=bill
            )

            return redirect(self.success_url)
        else:
            error_message = "The data provided is not valid."
            messages.error(request, error_message)
            return render(request, self.template_name, {'form': form, 'donut': donut})



@method_decorator(login_required, name='dispatch')
class ShoppingCartBuyView(View):
    template_name = 'shopping_cart/shopping_cart.html'
    succes_url = reverse_lazy('inventory:home')
    
    def get(self, request):
        cart_shopping_donuts = ShoppingCart.objects.filter(user=self.request.user) # replace with get_object_or_404
        donuts_details = []
        
        for cart_item in cart_shopping_donuts:
            donut = get_object_or_404(Donut, id=cart_item.donut.id )
            donuts_details.append({
                'name': donut.name,
                'price': donut.price,
                'quantity': cart_item.quantity,
                'total_price': cart_item.quantity * donut.price,
                'suggestion': cart_item.suggestion
            }) 
            
        context = {
            'donuts_details': donuts_details,
            'quantity_items_shopp': cart_shopping_donuts.count()
        }
        
        return render(request, self.template_name, context)

