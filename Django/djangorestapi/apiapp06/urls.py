from django.urls import path
from apiapp06 import views

urlpatterns = [
    path('blogs/',views.blog_view),

]
