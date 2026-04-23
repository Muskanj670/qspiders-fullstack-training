from django.urls import path
from authapp import views
from django.contrib.auth.views import PasswordChangeView

urlpatterns = [
    path('', views.home_view , name = "home"),
    path('about/', views.about_view , name = "about"),
    path('recent/', views.recent_view , name = "recent"),
    path('login/', views.login_view , name = "login"),
    path('signup/', views.signup_view , name = "signup"),
    path('logout/', views.logout_view , name = "logout"),
    path('change_password/',views.change_password, name = 'change_password'),
    path('reset_password/',
    PasswordChangeView.as_view(template_name = 'reset_password.html', success_url = '/'),
    name = 'reset_password')
]                     


