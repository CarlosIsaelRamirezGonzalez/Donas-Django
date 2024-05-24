from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField()    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is registered.')
        return email
    
    # def clean(self): Im not shure if this is necesary
    #     cleaned_data = super().clean()
    #     password1 = cleaned_data.get('password1')
    #     password2 = cleaned_data.get('password2')
    #     if password1 != password2:
    #         raise forms.ValidationError("Passwords don't match")
    #     return cleaned_data
    
    
class LoginForm(AuthenticationForm):
    email = forms.EmailField()
    
    class Meta:
        fields = ['email', 'password']
        