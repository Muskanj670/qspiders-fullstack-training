from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect, render

from authapp.forms import LoginForm, SignUpForm

def home_view(request):
    return render(request, "home.html")


@login_required(login_url="login")
def about_view(request):
    return render(request, "about.html")

@login_required(login_url="login")
def recent_view(request):
    return render(request, "recent.html")

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "User Created Successfully.")
            login(request, user)
            return redirect("home")
        messages.error(request, "Please correct the errors below.")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "Logged in successfully.")
                return redirect("home")
        messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("login")

@login_required(login_url="login")
def change_password(request):
    form = PasswordChangeForm(user=request.user)
    return render(request, "change_password.html", {"form": form})
