from django.urls import path
from apiapp05 import views

urlpatterns = [
    path('public/',views.public_view),
    path('private/',views.private_view),

]
