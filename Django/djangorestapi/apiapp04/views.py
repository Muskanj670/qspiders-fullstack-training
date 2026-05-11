from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.

class EmployeeModelAPI(viewsets.ModelViewSet):
    pass