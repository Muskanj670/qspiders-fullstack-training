from django.shortcuts import render
from .models import FeedbackModel
# Create your views here.

def form(request):
    submitted = False
    if request.method == 'POST':
        submitted = True
        name = request.POST['name']
        feedback = request.POST['feedback']
        FeedbackModel.objects.create(name = name, feedback= feedback)
    return render(request,'myapp/form.html',{'submitted':submitted})

def feedback(request):
    feedback = FeedbackModel.objects.all()
    context = {"feedbacks": feedback}
    return render(request,'myapp/feedback.html',context)


