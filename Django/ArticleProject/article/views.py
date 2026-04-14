from django.shortcuts import redirect, render
from .models import ArticleModel
from django.db.models import Q
# Create your views here.

def home(request):
    total_articles = ArticleModel.objects.count()
    total_authors = ArticleModel.objects.values('author').distinct().count()
    latest_articles = ArticleModel.objects.order_by('-created_at')[:6]
    return render(
        request,
        'article/home.html',
        {
            'total_articles': total_articles,
            'total_authors': total_authors,
            'latest_articles': latest_articles,
        },
    )

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
        article = ArticleModel.objects.filter(
            Q(title__icontains=search_query) | Q(content__icontains=search_query) | Q(author__icontains=search_query)
            ).order_by('-created_at')
    else:
        article = ArticleModel.objects.all().order_by('-created_at')
    return render(request,'article/allArticle.html',{'articles':article, 'search_query': search_query or ''})

def article_view(request,id):
    article = ArticleModel.objects.get(id = id)
    return render(request,'article/article.html',{'article': article})

def delete_article(request,id):
    article = ArticleModel.objects.get(id = id)
    if request.method == "POST":
        article.delete()
        return redirect('all-article')

    return render(request, 'article/confirm_delete.html', {'article': article})

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
    if request.method == "POST":
        article.delete()
    return redirect('all-article')

