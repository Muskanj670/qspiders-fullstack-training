from django.urls import path
from apiapp03 import views
from apiapp03.views import CustomerGetPostAPI, CustomerRUDAPI

urlpatterns = [
    path('customer/',CustomerGetPostAPI.as_view()),
    path('customer/<int:pk>/',CustomerRUDAPI.as_view()),

]
