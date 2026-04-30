from django.contrib import admin
from myapp.models import TODOModel

@admin.register(TODOModel)
class TODOModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'due_date', 'created_at')
    list_filter = ('status', 'due_date', 'created_at')
    search_fields = ('title', 'description')

