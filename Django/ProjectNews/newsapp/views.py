from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'newsapp/home.html')

def sports(request):
    news = {"type" : 'sports'}
    context = news
    return render(request,'newsapp/news.html', context)

def business(request):
    news = {"type" : 'business'}
    context = news
    return render(request,'newsapp/news.html', context)

def entertainment(request):
    news = {"type" : 'entertainment'}
    context = news
    return render(request,'newsapp/news.html', context)