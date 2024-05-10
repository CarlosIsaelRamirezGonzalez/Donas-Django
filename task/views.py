from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from .models import CarritoItem
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
                user = User.objects.create_user(username=username, password=password,email=email)
                user.save()
                return redirect("signup")
            except IntegrityError:
                return render(request,"registro.html",{
                    "error":"Username already exits"
                })
        else:
            return render(request,"registro.html",{
                    "error":"Username and password and email requeriment"
                })

def registrar(request):
    return render (request,("registro.html"))
def menu(request):
     return render (request,("menu.html"))
def signout(request):
      logout(request)
      return redirect("signup")
def order(request):
    
    return  render(request,"order.html")
def Terminos(request):
    
    return  render(request,"Terminos.html")

def registrardona(request):
    if request.method == "POST":
        cantidades = request.POST.get('cantdonas')
        pedido=CarritoItem.objects.create(cantidad=cantidades)
        # Aquí debes continuar con el resto de tu lógica para procesar la cantidad de donas
    else:
        # Manejar el caso en que la solicitud no sea de tipo POST, si es necesario
        pass
