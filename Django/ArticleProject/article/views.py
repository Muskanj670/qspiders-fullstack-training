from django.shortcuts import render
from .models import ArticleModel
# Create your views here.

def home(request):
    total_articles = ArticleModel.objects.count()
    latest_articles = ArticleModel.objects.order_by('-id')[:5]
    return render(request,'article/home.html', {'total_articles': total_articles, 'latest_articles': latest_articles})

def form(request):
    submitted = False
    if request.method == 'POST':
        submitted = True
        title = request.POST['title']
        content = request.POST['content']
        author = request.POST['author']
        ArticleModel.objects.create(title=title,content=content,author=author)
    return render(request,'article/form.html',{'submitted':submitted})

def allArticle(request):
    search_query = request.GET.get('search')
    if search_query:
        article = ArticleModel.objects.filter(title__icontains=search_query)
    else:
            article = ArticleModel.objects.all()
    return render(request,'article/allArticle.html',{'articles':article})

def article_view(request,id):
    article = ArticleModel.objects.get(id = id)
    return render(request,'article/article.html',{'article': article})

def delete_article(request,id):
    article = ArticleModel.objects.get(id = id)
    article.delete()
    return allArticle(request)

def update_article(request,id):
    article = ArticleModel.objects.get(id = id)
    if request.method == 'GET':
        return render(request,'article/update.html', {'article': article}) 
    if request.method == 'POST':
        article.title = request.POST['title']
        article.content = request.POST['content']
        article.author = request.POST['author']
        article.save()
        return article_view(request,id)

def delete_all(request):
    article = ArticleModel.objects.all()
    article.delete()
    return allArticle(request)

