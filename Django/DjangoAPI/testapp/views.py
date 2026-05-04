from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
# Create your views here.

students = [
    {
        'Name': "Muskan Jain",
        'Age': 23,
        'Subject': 'Django',
        'Addr': 'Agra'
    }
]

def student_view(request):
    return HttpResponse(f"{students[0]}")

@csrf_exempt
def api_view(request):
    if request.method == 'POST':
        try:
            student_data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        students.append(student_data)
        return JsonResponse(student_data, status=201)

    return JsonResponse(students, safe=False)

api = "http://127.0.0.1:8000/all/"
def fetch_data(request):
    data = requests.get(api).json()
    return render(request, 'data.html', {"data":data})

def post_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        subject = request.POST.get('subject')
        addr = request.POST.get('addr')

        student_data = {
            'Name' : name,
            'Age' : age,
            'Subject' : subject,
            'Addr' : addr
        }
        data = requests.post(api, json=student_data).json()
        return JsonResponse(data)
    return render(request, 'form.html')
