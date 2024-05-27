from django.contrib import admin
from django.urls import path, include
from Account import views

urlpatterns = [
    path('', views.index, name='index'), # I think we must to do a new app only for the index
    path('admin/', admin.site.urls),
    path('account/', include('Account.urls', namespace='account')),
    path('inventory/', include('Inventory.urls', namespace='inventory'))
]
