from django.urls import path
from newsapp import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('sports/',views.sports, name = 'sports'),
    path('business/',views.business, name = 'business'),
    path('entertainment/',views.entertainment, name = 'entertainment'),

]