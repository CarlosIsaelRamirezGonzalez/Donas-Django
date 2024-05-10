from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.shortcuts import render,redirect
from django.core.validators import validate_email
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from .models import CarritoItem,Cliente
from .models import Orden
from django.http import JsonResponse
from .models import Orden
from task.models import Producto, CarritoItem
from django.db import transaction
from copy import deepcopy
from .models import Cliente  # Asegúrate de que la ruta sea correcta según la estructura de tu proyecto
from django.shortcuts import render, redirect
# Create your views here.

def home(request):
    
    return  render(request,"home.html")
def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", {"form": UserCreationForm()})
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if username and password:  # Verifica si username y password tienen valores
            try:
                user=authenticate(request,username=username,password=password)
                if user is None:
                     return render(request,"signup.html",{
                      "error":"Username or password is incorrect"
                     })
                else:
                 login(request,user)
                 return redirect("menu")
            except:
                  return render(request,"signup.html",{
                    "error":"User already exits"
                })

        else:
              return render(request,"signup.html",{
                    "error":"Username and password requeriment"
                })

def registro(request):
    if request.method == "GET":
        return render(request, "registro.html", {"form": UserCreationForm()})
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email=request.POST.get("email")
        if username and password and email:  # Verifica si username y password tienen valores
            try:
                validate_email(email)
                user = User.objects.create_user(username=username, password=password,email=email)
                user.save()
                return redirect("signup")
            except:
                return render(request,"registro.html",{
                    "error":"Username already exits or email is wrong"
                })
        else:
            return render(request,"registro.html",{
                    "error":"Username and password and email requeriment"
                })

def registrar(request):
    return render (request,("registro.html"))
def menu(request):
     quantity = CarritoItem.objects.count()
     return render (request,"menu.html", {
         'quantity': quantity,
     })
def signout(request):
      logout(request)
      return redirect("signup")
def order(request):
    
    return  render(request,"order.html")


def Terminos(request):
    
    return  render(request,"Terminos.html")




def registrardona(request):
    if request.method == "POST":
        cantidades_str = request.POST.get('cantdonas')
        if cantidades_str:
            cantidades = int(cantidades_str)
            id_producto_deseado = 4
            producto_deseado = Producto.objects.get(pk=id_producto_deseado)
            total = producto_deseado.precio * cantidades
            pedido = CarritoItem.objects.create(cantidad=cantidades, producto=producto_deseado, total=total)
            # Aquí puedes continuar con el resto de tu lógica para procesar la cantidad de donas
            # Por ejemplo, podrías redirigir al usuario a otra página o renderizar un template con un mensaje de confirmación
            return redirect('menu')  # Reemplaza 'ruta_a_otra_pagina' por la URL a la que quieres redirigir al usuario
        else:
            # Manejar el caso en que no se proporciona una cantidad de donas
            # Por ejemplo, puedes renderizar un template con un mensaje de error
            return render(request, 'template_con_mensaje_de_error.html', {'error': 'No se proporcionó una cantidad de donas'})
    else:
        # Manejar el caso en que la solicitud no sea de tipo POST, si es necesario
        # Por ejemplo, puedes redirigir al usuario a otra página o renderizar un template con un formulario para ingresar la cantidad de donas
        return render(request, 'template_con_formulario_de_cantidad_de_donas.html')
    
def registrardonaBrownie(request):
    if request.method == "POST":
        cantidades_str = request.POST.get('cantdonas')
        if cantidades_str:
            cantidades = int(cantidades_str)
            id_producto_deseado = 1
            producto_deseado = Producto.objects.get(pk=id_producto_deseado)
            total = producto_deseado.precio * cantidades
            pedido = CarritoItem.objects.create(cantidad=cantidades, producto=producto_deseado, total=total)
            # Aquí puedes continuar con el resto de tu lógica para procesar la cantidad de donas
            # Por ejemplo, podrías redirigir al usuario a otra página o renderizar un template con un mensaje de confirmación
            return redirect('menu')  # Reemplaza 'ruta_a_otra_pagina' por la URL a la que quieres redirigir al usuario
        else:
            # Manejar el caso en que no se proporciona una cantidad de donas
            # Por ejemplo, puedes renderizar un template con un mensaje de error
            return render(request, 'template_con_mensaje_de_error.html', {'error': 'No se proporcionó una cantidad de donas'})
def registrarcanela(request):
    if request.method == "POST":
        cantidades_str = request.POST.get('cantdonas')
        if cantidades_str:
            cantidades = int(cantidades_str)
            id_producto_deseado = 3
            producto_deseado = Producto.objects.get(pk=id_producto_deseado)
            total = producto_deseado.precio * cantidades
            pedido = CarritoItem.objects.create(cantidad=cantidades, producto=producto_deseado, total=total)
            # Aquí puedes continuar con el resto de tu lógica para procesar la cantidad de donas
            # Por ejemplo, podrías redirigir al usuario a otra página o renderizar un template con un mensaje de confirmación
            return redirect('menu')  # Reemplaza 'ruta_a_otra_pagina' por la URL a la que quieres redirigir al usuario
        else:
            # Manejar el caso en que no se proporciona una cantidad de donas
            # Por ejemplo, puedes renderizar un template con un mensaje de error
            return render(request, 'template_con_mensaje_de_error.html', {'error': 'No se proporcionó una cantidad de donas'})       

def registrardonaclassic(request):
    if request.method == "POST":
        cantidades_str = request.POST.get('cantdonas')
        if cantidades_str:
            cantidades = int(cantidades_str)
            id_producto_deseado = 2
            producto_deseado = Producto.objects.get(pk=id_producto_deseado)
            total = producto_deseado.precio * cantidades
            pedido = CarritoItem.objects.create(cantidad=cantidades, producto=producto_deseado, total=total)
            # Aquí puedes continuar con el resto de tu lógica para procesar la cantidad de donas
            # Por ejemplo, podrías redirigir al usuario a otra página o renderizar un template con un mensaje de confirmación
            return redirect('menu')  # Reemplaza 'ruta_a_otra_pagina' por la URL a la que quieres redirigir al usuario
        else:
            # Manejar el caso en que no se proporciona una cantidad de donas
            # Por ejemplo, puedes renderizar un template con un mensaje de error
            return render(request, 'template_con_mensaje_de_error.html', {'error': 'No se proporcionó una cantidad de donas'})
        



def Domicilio(request):
    if request.method == "POST":
        Address = request.POST.get('Address')
        Estado = request.POST.get('State')
        Code = request.POST.get('Postal')
        usuario = request.user
        try:
            cliente = Cliente.objects.get(usuario=usuario)
            cliente.address = Address
            cliente.estate = Estado
            cliente.postalcode = Code
            cliente.save()
        except Cliente.DoesNotExist:
            cliente = Cliente.objects.create(usuario=usuario, address=Address, estate=Estado, postalcode=Code)
        return redirect('shopping')
    else:
        carrito_items = CarritoItem.objects.all()
        total = sum(item.total for item in carrito_items)
        return render(request, 'shopping.html', {'carrito_items': carrito_items, 'total': total})

def shopping(request):
    carrito_items = CarritoItem.objects.all()
    total = sum(item.total for item in carrito_items)
    return render(request, 'shopping.html', {'carrito_items': carrito_items, 'total': total})
def eliminar_producto(request, item_id):
    item = get_object_or_404(CarritoItem, pk=item_id)
    item.delete()
    return redirect('shopping')






def comprar(request):
    if request.method == "POST":
        # Obtener el cliente actual
        usuario = request.user
        try:
            cliente = Cliente.objects.get(usuario=usuario)
        except Cliente.DoesNotExist:
            # Si el cliente no existe, redirigir al usuario a la página de registro de domicilio
            return redirect('Domicilio')
        
        carrito_items = CarritoItem.objects.all()

        # Crear una nueva orden
        nombres_productos = ', '.join(item.producto.nombre for item in carrito_items)
        total = sum(item.total for item in carrito_items)
        orden = Orden.objects.create(
            cliente=cliente,
            productos=nombres_productos,
            total=total,
            fecha=timezone.now()
        )

        # Limpiar el carrito de compras
        CarritoItem.objects.all().delete()

        return redirect('orders')
    else:
        return redirect('Terminos')
def orders(request):
    ordenes = Orden.objects.all()
    context = {
        'ordenes': ordenes
    }
    return render(request, "orders.html", context)