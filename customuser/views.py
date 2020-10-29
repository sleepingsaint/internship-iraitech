from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from customuser.admin import UserCreationForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def loginView(req):
    if(req.method == "POST"):
        email = req.POST.get("username")
        password = req.POST.get("password")
        user = authenticate(username=email, password=password)
        if user is not None:
            login(req, user)
            return redirect('/api/v1/calculate')
        messages.error(req, "Invalid email and password")

    form = AuthenticationForm()
    return render(req, 'customuser/login.html', {"form": form})


def signup(req):
    if(req.method == "POST"):
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('/api/v1/calculate')
        messages.error(req, "email is already taken")

    form = UserCreationForm()
    return render(req, 'customuser/signup.html', {"form": form})


@login_required
def logoutView(req):
    logout(req)
    return redirect('/accounts/login')
