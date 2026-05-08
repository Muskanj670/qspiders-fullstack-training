from django.urls import path
from apiapp02 import views
from apiapp02.views import EmployeeAPI

urlpatterns = [
    path('employee/',EmployeeAPI.as_view()),
    path('employee/<int:id>/',EmployeeAPI.as_view()),

]
