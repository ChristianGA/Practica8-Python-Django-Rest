from django import forms
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class LoginForm(forms.Form):

    login_username = forms.CharField(label="Nombre de usuario")
    login_password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")

class SignupForm(ModelForm):

    class Meta:
        model = User
        fields = '__all__'