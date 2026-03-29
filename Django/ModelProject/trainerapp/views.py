from django.shortcuts import render
from .models import TrainerModel

# Create your views here.
def trainers(request):
    data = TrainerModel.objects.all() 
    context = {'trainers': data}
    return render(request,"trainerapp/trainers.html",context)
