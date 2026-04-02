from django.shortcuts import render
from .models import FeedbackModel
# Create your views here.

def home(request):
    return render(request,'myapp/index.html')

def form(request):
    submitted = False
    if request.method == 'POST':
        submitted = True
        name = request.POST['name']
        feedback = request.POST['feedback']
        FeedbackModel.objects.create(name = name, feedback= feedback)
    return render(request,'myapp/form.html',{'submitted':submitted})

def feedback(request):
    search_query = request.GET.get('search')
    if search_query:
        feedback = FeedbackModel.objects.filter(name__icontains = search_query)
    else:
        feedback = FeedbackModel.objects.all()
    context = {"feedbacks": feedback}
    return render(request,'myapp/feedback.html',context)


