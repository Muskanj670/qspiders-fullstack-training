from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import studentModel
from .serializers import studentModelSerializer

# Create your views here.
"""
! Django Rest FrameWork
It is a powerful toolkit built on the top of the django to build web apps.

! Serialization
Process of converting data into Json Data

! Deserialozation
Converting JSON data into meaningful data
"""


@api_view(['GET', 'POST'])
def student_view(request):
    if request.method == 'GET':
        students = studentModel.objects.all()
        serializer = studentModelSerializer(students, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = studentModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET', 'PUT','PATCH', 'DELETE'])
def specific_student(request, id):
    try:
        student = studentModel.objects.get(id = id)
    except student.DoesNotExist:
        return Response({"MESSGAE" : f'Student with id {id} doest not found.'}, status = status.HTTP_404_NOT_FOUND) 
    serializer = studentModelSerializer(student)
    if request.method == 'GET':
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = studentModelSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = studentModelSerializer(student, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        

