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

def context(request):
    data = {
        'Name' : "Muskan Jain",
        'Age' : 21,
        'Course' : 'Python FullStack'
    }
    return render(request,"studentapp/context.html",context=data)


def context2(request):
    data = {
        'Stu1': {
            'Name': "Muskan Jain",
            'Age': 22,
            'Course': 'Python FullStack'
        },
        'Stu2' : {
            'Name': "Amrita Singh",
            'Age': 24,
            'Course': 'Data Analyst'
        }
    }
    return render(request, "studentapp/context2.html", {'context': data})

def context3(request):
    news = {
        'type' : 'sports'
    }
    return render(request,'studentapp/context3.html', context=news)