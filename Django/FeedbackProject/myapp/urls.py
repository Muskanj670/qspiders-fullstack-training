from django.urls import path
from myapp import views

urlpatterns = [
    path('form/', views.form),
    path('feedback/',views.feedback)

]