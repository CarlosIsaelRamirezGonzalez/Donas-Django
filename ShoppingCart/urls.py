from django.urls import path
from . import views

app_name = 'shopping_cart'

urlpatterns = [
    path('shoping_form/<int:donut_id>', views.ShoppingFormView.as_view(), name="shoping_form"), # The view is missing
    path('shopping_cart_buy', views.ShoppingCartBuyView.as_view(), name='shopping_cart_buy'),
]