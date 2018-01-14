from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):

    login_username = forms.CharField(label="Nombre de usuario")
    login_password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")

class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']