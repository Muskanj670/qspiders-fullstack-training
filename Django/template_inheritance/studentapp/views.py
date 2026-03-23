from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,"index.html")

def exam(request):
    return render(request,"studentapp/exam.html")

def attendence(request):
    return render(request, "studentapp/attendence.html")

def holiday(request):
    return render(request, "studentapp/holiday.html")
