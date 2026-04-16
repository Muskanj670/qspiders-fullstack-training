from django.shortcuts import render
from authapp.forms import SignUpForm

# Create your views here.

def home_view(request):
    return render(request , "authapp/home.html")

def about_view(request):
    return render(request , "authapp/about.html")
    

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
            form = SignUpForm()
    else:
        form = SignUpForm()
    return render(request , "authapp/signup.html",{'form':form})
    

def login_view(request):
    
    return render(request , "authapp/login.html")
    
