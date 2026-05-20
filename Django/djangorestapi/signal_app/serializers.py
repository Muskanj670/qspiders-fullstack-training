from .models import BlogSignal
from rest_framework import serializers

class BlogSignalSer(serializers.ModelSerializer):
    class Meta:
        model = BlogSignal
        fields = "__all__"