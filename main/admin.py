from django.contrib import admin

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name','user','date_time']
    ordering = ['-date_time']

    
admin.site.register(Article,ArticleAdmin)
