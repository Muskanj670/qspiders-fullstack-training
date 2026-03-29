from django.urls import path
from modelapp import views

urlpatterns = [
    path('students/', views.students),

]