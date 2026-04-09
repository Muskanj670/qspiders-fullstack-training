from django.contrib import admin
from .models import ArticleModel
# Register your models here.

class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','content','created_at','updated_at')
admin.site.register(ArticleModel,ArticleModelAdmin)