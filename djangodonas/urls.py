"""djangodonas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task import views
from task.views import registrardona
from task.views import registrardonaBrownie
from task.views import registrarcanela
from task.views import registrardonaclassic,Domicilio
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.signup, name="home"),
    path("signup/", views.signup, name="signup"),
    path("registro/", views.registro, name="registro"),
    path("registrar/", views.registrar, name="registrar"),
    path("menu/", views.menu, name="menu"),
    path("order/", views.order, name="order"),
    path("Terminos/", views.Terminos, name="Terminos"),
    path("logut/", views.signout, name="logout"),
    path("registrardona/",registrardona),
    path("registrardonaBrownie/",registrardonaBrownie),
    path("registrardonacanela/",registrarcanela),
    path("registrardonaclassic/",registrardonaclassic, name="registrardonaclassic"),
    path("Domicilio/",Domicilio),
    path('shopping/', views.shopping, name='shopping'),
    path('eliminar_producto/<int:item_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('comprar/', views.comprar, name='comprar'),
path('orders/', views.orders, name='orders'),
    # Cambiado a views.registrar
]