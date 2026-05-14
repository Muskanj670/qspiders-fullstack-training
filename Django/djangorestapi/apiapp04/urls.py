from django.urls import path, include
from apiapp03 import views
from apiapp04.views import EmployeeModelAPI
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('employee', EmployeeModelAPI)
urlpatterns = [
    path('',include(router.urls)),
    # path('employee/<int:pk>/',CustomerRUDAPI.as_view()),

]
