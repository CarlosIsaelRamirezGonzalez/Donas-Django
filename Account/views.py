from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, LoginForm
from django.views.generic import FormView

class SignUpView(FormView):
    template_name = 'account/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)
    
    def form_invalid(self, form):
        errors = form.errors.as_data()
        error_message = "The data provided is not valid."
        
        if 'email' in errors:
            email_errors = errors['email']
            error_message = email_errors[0].message
            
        messages.error(self.request, error_message) # Add the error message to the context
        return self.render_to_response(self.get_context_data(form=form)) # Deploy the template with the errros
        
class LoginView(FormView):
    template_name = 'account/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        user = authenticate(username = form.cleaned_data['username'],
                            password = form.cleaned_data['password'],)
        if user is not None:
            login(self.request, user)
            return redirect(self.success_url)
        else:
            error_message = 'This username does not exists or te password is wrong.'
            messages.error(self.request, error_message)
            return self.render_to_response(self.get_context_data(form=form))
    
    def form_invalid(self, form):
        error_message = "The data provided is not valid."
        
        messages.error(self.request, error_message)
        return self.render_to_response(self.get_context_data(form=form))
        
@login_required
def logout_view(request):
    logout(request)
    return redirect('index')    

def index(request):
    return render(request, 'account/index.html')