from django.urls import path
from article import views
urlpatterns = [
    path('',views.home,name = 'home'),
    path('form/',views.form, name = 'form'),
    path('all-article/',views.allArticle,name = 'all-article'),
    path('article/<int:id>/',views.article_view,name = 'article'),
    path('delete/<int:id>/',views.delete_article,name = 'delete'),
    path('delete_all/',views.delete_all, name = 'delete_all'),
    path('update/<int:id>/', views.update_article, name='update_article'),
    
]