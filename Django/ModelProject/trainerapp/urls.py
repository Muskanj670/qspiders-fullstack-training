from django.urls import path
from trainerapp import views

urlpatterns = [
    path('trainers/', views.trainers),

]