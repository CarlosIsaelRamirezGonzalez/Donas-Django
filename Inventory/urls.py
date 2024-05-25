from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('terms_and_conditions/', views.terms_and_conditions, name="terms_and_conditions") # Sounds weird
]