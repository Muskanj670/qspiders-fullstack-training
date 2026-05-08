from django.shortcuts import render
from .serializers import CustomerSerializer
from .models import Customer
from rest_framework import generics, mixins

# Create your views here.

class CustomerGetPostAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class CustomerRUDAPI(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

"""
! generics:
    ? GenericAPIView :
        -

! mixins
    ? ListModelMixin :
        - list() -> Get method
    ? CreateModelMixin
        - create() -> post method
"""