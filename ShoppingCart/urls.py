from django.urls import path
from . import views

app_name = 'shopping_cart'

urlpatterns = [
    path('shoping_form/<int:donut_id>', views.ShoppingFormView.as_view(), name="shoping_form"), # The view is missing
    path('shopping_cart_buy', views.ShoppingCartBuyView.as_view(), name='shopping_cart_buy'),
    path('delete_shopping/<int:shopping_id>', views.ShoppingCartDeleteView.as_view(), name='shopping_cart_delete'),
    path('edit_shopping/<int:shopping_id>', views.ShoppingCartEditView.as_view(), name='shopping_cart_edit'),
    path('user_orders/', views.UserOrders.as_view(), name='user_orders'),
    path('shopping_address_form/', views.AddressFormView.as_view(), name='shopping_address_form'),
]