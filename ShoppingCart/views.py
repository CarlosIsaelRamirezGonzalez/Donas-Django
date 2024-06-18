from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# from .functions import generateAccessToken,create_order,capture_order
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework.permissions import AllowAny
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.conf import settings
from datetime import datetime
from rest_framework.views import APIView
from rest_framework import status
from django.contrib import messages
from django.views import View
from Inventory.models import Donut
from django.urls import reverse_lazy
from Inventory.models import Profits
from .models import ShoppingCart, Order
from .forms import ShoppingForm, AddressForm


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
class UserOrders(View):
    template_name = 'shopping_cart/user_orders.html'

    def get(self, request):
        user_orders = Order.objects.filter(user=request.user)
        
        context = {
            'user_orders': user_orders
        }
        
        return render(request, self.template_name, context)
    
    


@method_decorator(login_required, name='dispatch')
class AddressFormView(View):
    template_name = 'shopping_cart/shopping_address_form.html'

    def get(self, request):
        form = AddressForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = AddressForm(request.POST)
        if form.is_valid():
            # Crear una instancia del objeto Order
            order = form.save(commit=False)
            
            # Asignar el usuario actual
            order.user = request.user

            # Calcular el total de la orden
            total_amount = 0
            user_shopping_cart = ShoppingCart.objects.filter(user=request.user)
            for cart_item in user_shopping_cart:
                total_amount += cart_item.quantity * cart_item.donut.price
            
            # Crear objetos Order basados en el carrito de compras del usuario
            user_shopping_cart = ShoppingCart.objects.filter(user=request.user)
            for cart_item in user_shopping_cart:
                order_item = Order.objects.create(
                    address=order.address,
                    quantity=cart_item.quantity,  # Asignar la cantidad del carrito de compras
                    status=Order.Status.PROCESS,  # Puedes cambiar el estado según sea necesario
                    user=request.user,
                    donut=cart_item.donut,
                    suggestion=cart_item.suggestion
                )
                order_item.save()
                
            # Enviar el correo electrónico con los detalles de la orden
            subject = 'Recibo de tu compra en La Dona Glaseada'
            message = f'Hola {request.user.username},\n\nGracias por tu compra en La Dona Glaseada. Aquí está el resumen de tu orden:\n\n'
            message += f'Fecha de la orden: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n'
            message += f'Cantidad total pagada: {total_amount}\n\n'
            message += 'Detalles de la orden:\n\n'
            for cart_item in user_shopping_cart:
                message += f'- {cart_item.quantity}x {cart_item.donut.name}\n'
            message += '\n¡Gracias por tu compra!'
            
            send_mail(subject, message, settings.EMAIL_HOST_USER, [request.user.email])
            profit = Profits.objects.create(
                profit = total_amount,
                user = request.user
            )
            profit.save()
                
            # Limpiar el carrito de compras después de crear las órdenes
            user_shopping_cart.delete()
            
            # Redirigir a una página de confirmación o a donde desees
            return redirect('inventory:home')  # Reemplaza 'ruta_hacia_pagina_de_confirmacion' con la ruta adecuada
        else:
            # Si el formulario no es válido, renderizar nuevamente el formulario con los errores
            context = {
                'form': form
            }
            return render(request, self.template_name, context)


@method_decorator(login_required, name='dispatch')
class ShoppingCartBuyView(View):
    template_name = 'shopping_cart/shopping_cart.html'
    succes_url = reverse_lazy('inventory:home')
    
    def get(self, request):
        cart_shopping_donuts = ShoppingCart.objects.filter(user=self.request.user) # replace with get_object_or_404
        donuts_details = []
        subtotal = 0

        for cart_item in cart_shopping_donuts:
            donut = get_object_or_404(Donut, id=cart_item.donut.id )
            total_price = cart_item.quantity * donut.price
            subtotal += total_price
            donuts_details.append({
                'name': donut.name,
                'price': donut.price,
                'quantity': cart_item.quantity,
                'total_price': total_price,
                'suggestion': cart_item.suggestion,
                'id': cart_item.id,
            }) 
            
        context = {
            'donuts_details': donuts_details,
            'quantity_items_shopp': cart_shopping_donuts.count(),
            'subtotal': subtotal,

        }
        
        return render(request, self.template_name, context)



# Poner el required POST
@method_decorator(login_required, name='dispatch')
class ShoppingCartDeleteView(View):
    
    def get(self, request, shopping_id):
        shopping_cart_item = get_object_or_404(ShoppingCart, id=shopping_id)
        shopping_cart_item.delete()
        return redirect('shopping_cart:shopping_cart_buy')  
    
    
    
@method_decorator(login_required, name='dispatch')
class ShoppingCartEditView(View):
    
    def get(self, request, shopping_id):
        shopping_cart_item = get_object_or_404(ShoppingCart, id=shopping_id)
        form = ShoppingForm(instance=shopping_cart_item)
        return render(request, 'shopping_cart/shopping_cart_edit.html', {'form': form, 'shopping_cart_item': shopping_cart_item})
    
    def post(self, request, shopping_id):
        shopping_cart_item = get_object_or_404(ShoppingCart, id=shopping_id)
        form = ShoppingForm(request.POST, instance=shopping_cart_item)
        if form.is_valid():
            form.save()
            return redirect('shopping_cart:shopping_cart_buy')  # Redirigir a la lista del carrito de compras o a otra vista
        return render(request, 'shopping_cart/shopping_cart_edit.html', {'form': form, 'shopping_cart_item': shopping_cart_item})
    
    
    
# @method_decorator(csrf_exempt, name='dispatch')
# class CrearOrden(APIView):
#     def post(self, request, *args, **kwargs):
#         user = request.user
#         cliente = Cliente.objects.get(usuario=user)
#         carrito_items = CarritoItem.objects.filter(cliente=cliente)

#         total = sum(item.total for item in carrito_items)
#         productos = ", ".join([item.producto.nombre for item in carrito_items])

#         # Crear una orden usando la función personalizada
#         order_response = create_order(productos)

#         if order_response and 'id' in order_response:
#             orden = Orden.objects.create(cliente=cliente, productos=productos, total=total)
#             return JsonResponse(order_response)
#         else:
#             return JsonResponse({'error': 'Falló la creación de la orden'}, status=500)
        
@method_decorator(csrf_exempt, name='dispatch')
class CapturarOrdenPaypal(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, *args, **kwargs):
       
        try:
            # Recuperar por url
            order_id = self.kwargs['order_id']
            response = capture_order(order_id)
            return Response(response, status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            return Response({"error": "error aqui"}, status=status.HTTP_400_BAD_REQUEST)
    