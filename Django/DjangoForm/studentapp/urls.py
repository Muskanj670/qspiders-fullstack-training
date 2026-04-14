from django.urls import path
from studentapp import views
urlpatterns = [
    path('',views.form_view),
    path('login/',views.login_view),
    path('details/',views.details,name = 'all'),
    path('delete/<int:id>',views.delete_view, name = 'delete'),
    path('update/<int:id>',views.update_view, name = 'update')

]