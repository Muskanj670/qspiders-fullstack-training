from django.shortcuts import render, redirect
from studentapp.models import StudentModel
from studentapp.forms import StudentForm,studentLoginForm

# Create your views here.

def form_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    form = StudentForm()
    return render(request, 'studentapp/form.html',{'form':form})

def login_view(request):
    form = studentLoginForm()
    return render(request,"studentapp/login.html",{"form":form})

def details(request):
    data = StudentModel.objects.all()
    return render(request,"studentapp/details.html", {"data":data})

def delete_view(request, id):
    data = StudentModel.objects.get(id = id)
    if request.method == 'POST':
        data.delete()
        return details(request)
    return render(request,'studentapp/confirm_delete.html',{"data":data})


def update_view(request, id):
    data = StudentModel.objects.get(id = id)
    if request.method == 'POST':
        form = StudentForm(request.POST , instance=data)
        if form.is_valid():
            form.save()
            return redirect("all")
    
    form = StudentForm(instance=data)
    return render(request,"studentapp/update_form.html",{'form':form})
