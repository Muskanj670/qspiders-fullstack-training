from . import views
from django.urls import path

urlpatterns = [
    path('student/', views.student_view, name = 'student'),
    path('all/', views.api_view, name = 'api'),
    path("fetch/", views.fetch_data, name = 'fetch'),
    path("post/", views.post_data, name = 'post')
]
