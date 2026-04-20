from django.shortcuts import render, redirect
from authapp.forms import SignUpForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def home_view(request):
    return render(request , "authapp/home.html")

@login_required(login_url='login')
def about_view(request):
    return render(request , "authapp/about.html")
    
@login_required(login_url='login')
def recent_view(request):
    return render(request , "authapp/recent.html")
    

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            s = form.save(commit=False)
            password = form.cleaned_data['password']
            s.set_password(password)
            form.save()
            messages.success(request, 'signed up successfully....!')
            return redirect("login")
    else:
        form = SignUpForm()
    return render(request , "authapp/signup.html",{'form':form})
    

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u , password = p)
            if user == None:
                messages.warning(request,'Invalid credential...❌')
            else:
                login(request,user)
                messages.success(request, "Logged in Successfully...✅")
                return redirect("home")
    form = LoginForm()
    return render(request , "authapp/login.html",{'form':form})

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully....✅")
    return redirect('login')
    
