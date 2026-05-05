from django.urls import path
from apiapp01 import views

urlpatterns = [
    path('students/', views.student_view, name = 'student'),
    path('specific/<int:id>', views.specific_student)
]
