from django.urls import path
from studentapp import views

urlpatterns = [
    path("base/",views.base),
    path('exam/',views.exam),
    path('attendence/',views.attendence),
    path('holiday/',views.holiday),
    path('context/',views.context),
    path('context2/',views.context2),
    path('context3/',views.context3),
]