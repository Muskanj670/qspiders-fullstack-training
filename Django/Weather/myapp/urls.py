from django.urls import path
from myapp import views

urlpatterns = [
    path('today/', views.today, name = 'today'),
    path('joke/', views.joke, name = 'joke'),
]