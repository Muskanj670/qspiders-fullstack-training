from django.shortcuts import render
from studentapp.models import StudentModel
from studentapp.forms import StudentForm,studentLoginForm

# Create your views here.

def form_view(request):
    form = StudentForm()
    return render(request, 'studentapp/form.html',{'form':form})

def login_view(request):
    form = studentLoginForm()
    return render(request,"studentapp/login.html",{"form":form})
