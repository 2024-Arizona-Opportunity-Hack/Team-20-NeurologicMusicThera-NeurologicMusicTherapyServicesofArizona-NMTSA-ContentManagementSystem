from django.db import models
from django.db.models import ManyToManyField
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

class AccessGroup(models.Model):
    group_name = models.CharField(max_length=400)
    users = ManyToManyField(User)

class VideoContent(models.Model):
    title = models.CharField(max_length=400)
    video_file = models.FileField(upload_to="content/videos")
    transcript = models.TextField(default="No transcript available")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.TextField()
    access_groups = models.ManyToManyField(AccessGroup)

class Article(models.Model):
    title = models.CharField(max_length=400)
    article = models.FileField(upload_to="content/articles")
    transcript = models.TextField(default="No transcript available")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.TextField()
    access_groups = models.ManyToManyField(AccessGroup)

