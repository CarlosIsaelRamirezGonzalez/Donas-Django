from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
]