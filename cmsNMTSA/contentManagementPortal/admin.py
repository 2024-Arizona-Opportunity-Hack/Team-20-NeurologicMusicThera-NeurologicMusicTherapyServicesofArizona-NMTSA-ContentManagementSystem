from django.contrib import admin
from .models import VideoContent, Article, Category, AccessGroup
# Register your models here.

admin.site.register(VideoContent)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(AccessGroup)