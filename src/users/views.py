from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from users.forms import LoginForm, SignupForm


class loginView(View):

    def get(self, request):
        context = {'form': LoginForm()}
        return render(request, "login_form.html", context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("login_username")
            password = form.cleaned_data.get("login_password")
            authenticated_user = authenticate(username=username, password=password)
            if authenticated_user and authenticated_user.is_active:
                django_login(request, authenticated_user)
                redirect_to = request.GET.get("next", "home_page")
                return redirect(redirect_to)
            else:
                messages.error(request, "Usuario incorrecto o inactivo")
        return render(request, "login_form.html", {'form': form})

def logout(request):
    django_logout(request)
    return redirect("login_page")

class signupView(View):

    def get(self, request):
        context = {'form': SignupForm()}
        return render(request, "signup_form.html", context)

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_page")
        else:
            messages.error(request, "Vuelva a intentarlo")
        return render(request, "signup_form.html", {'form': form})