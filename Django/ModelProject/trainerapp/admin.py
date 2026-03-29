from django.contrib import admin
from .models import TrainerModel

# Register your models here.
class TrainerModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','subject','email','address']
admin.site.register(TrainerModel,TrainerModelAdmin)

