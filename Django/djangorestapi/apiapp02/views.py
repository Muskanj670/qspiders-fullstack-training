from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import EmployeeModel
from .serializers import empModelSerializer
from rest_framework.views import APIView

# Create your views here.

class EmployeeAPI(APIView):
    def get(self,request, id = None):
        if id:
            try:
                emp = EmployeeModel.objects.get(id = id)
                serializer = empModelSerializer(emp)
                return Response(serializer.data)
            except EmployeeModel.DoesNotExist:
                return Response(status = status.HTTP_404_NOT_FOUND)
        else:
            emp = EmployeeModel.objects.all()
            serializer = empModelSerializer(emp,many = True)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = empModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)
    
    def put(self,request, id):
        try:
            emp = EmployeeModel.objects.get(id = id)
            serializer = empModelSerializer(emp, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(status = status.HTTP_400_BAD_REQUEST)
        except EmployeeModel.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        
    def patch(self,request, id):
        try:
            emp = EmployeeModel.objects.get(id = id)
            serializer = empModelSerializer(emp, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(status = status.HTTP_400_BAD_REQUEST)
        except EmployeeModel.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        
    def delete_emp(self,request, id):
        emp = EmployeeModel.objects.get(id = id)
        emp.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)        

 
