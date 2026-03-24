from django.urls import path
from newsapp import views

urlpatterns = [
    path('home/', views.home),
    path('sports/',views.sports),
    path('business/',views.business),
    path('entertainment/',views.entertainment),

]