from django.urls import path
from signal_app import views

urlpatterns = [
    path('',views.blog_view),
    # path('employee/<int:pk>/',CustomerRUDAPI.as_view()),

]
