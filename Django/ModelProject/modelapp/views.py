from django.shortcuts import render
from .models import StudentModel

# Create your views here.
def students(request):
    data = StudentModel.objects.all() 
    context = {'students': data}
    return render(request,"modelapp/students.html",context)
