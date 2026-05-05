from rest_framework import serializers
from apiapp01.models import studentModel

class studentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentModel
        fields = '__all__'