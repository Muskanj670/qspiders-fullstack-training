
from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.home_view , name = 'home'),
    path('signup/', views.signup_view , name = 'signup'),
    path('login/', views.login_view , name = 'login'),
    path('logout/', views.logout_view , name = 'logout'),
    path('task/', views.task_view , name = 'task'),
    path('task/<int:pk>/edit/', views.update_task_view , name = 'update_task'),
    path('task/<int:pk>/complete/', views.complete_task_view , name = 'complete_task'),
    path('task/<int:pk>/delete/', views.delete_task_view , name = 'delete_task'),
]
