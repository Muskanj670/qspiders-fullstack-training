from rest_framework import serializers
from apiapp02.models import EmployeeModel

class empModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = "__all__"