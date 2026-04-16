from django.urls import path
from authapp import views

urlpatterns = [
    path('home/', views.home_view , name = "home"),
    path('about/', views.about_view , name = "about"),
    path('recent/', views.recent_view , name = "recent"),
    path('login/', views.login_view , name = "login"),
    path('signup/', views.signup_view , name = "signup"),

]