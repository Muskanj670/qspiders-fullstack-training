from django.urls import path
from studentapp import views
urlpatterns = [
    path('',views.form_view),
    path('login/',views.login_view)
]