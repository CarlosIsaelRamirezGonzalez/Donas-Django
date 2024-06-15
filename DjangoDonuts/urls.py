from django.contrib import admin
from django.urls import path, include
from Index import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('admin/', admin.site.urls),
    path('account/', include('Account.urls', namespace='account')),
    path('inventory/', include('Inventory.urls', namespace='inventory')),
    path('shopping_cart/', include('ShoppingCart.urls', namespace='shopping_cart')),
]
