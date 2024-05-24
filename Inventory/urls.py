from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('/', views.SignUpView.as_view(), name='index'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('terms/', views.terms, name="terms") # Sounds weird
]