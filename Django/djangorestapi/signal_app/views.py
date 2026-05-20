from django.shortcuts import render
from .models import BlogSignal
from .serializers import BlogSignalSer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET',"POST"])
def blog_view(request):
    if request.method == 'POST':
        serializer = BlogSignalSer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error_messages)
    
    if request.method == 'GET':
        blogs = BlogSignal.objects.all()
        serializer = BlogSignalSer(blogs, many = True)
        return Response(serializer.data)
