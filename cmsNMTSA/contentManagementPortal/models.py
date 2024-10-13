from django.db import models
from django.db.models import ManyToManyField
from django.contrib.auth.models import User, Group
from django.utils import timezone
import uuid, os
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class AccessGroup(models.Model):
    group_name = models.CharField(max_length=400, unique=True)
    users = ManyToManyField(User)
    permissions_description = models.CharField(max_length=500)

    def __str__(self):
        return self.group_name

def generate_new_filename(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f"{uuid.uuid4().hex}.{ext}"
    if ext == "mp4":
        return os.path.join('content/videos', new_filename)
    elif ext == "docx" or ext == "pdf":
        return os.path.join('content/articles', new_filename)
    elif ext=="png" or ext == "jpg" or ext =="jpeg" or ext == "webp":
        return os.path.join('content/thumbnails', new_filename)

class VideoContent(models.Model):
    title = models.CharField(max_length=400)
    video_file = models.FileField(upload_to=generate_new_filename)
    transcript = models.TextField(default="No transcript available")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    access_groups = models.ManyToManyField(AccessGroup)
    thumbnail = models.ImageField(upload_to=generate_new_filename, null=True, blank=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.PROTECT)
    uploaded_on = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.title} | {self.uploaded_by} | {self.uploaded_on}"

class Article(models.Model):
    title = models.CharField(max_length=400)
    article = models.FileField(upload_to=generate_new_filename)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    access_groups = models.ManyToManyField(AccessGroup)
    thumbnail = models.ImageField(upload_to=generate_new_filename, null=True, blank=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.PROTECT)
    uploaded_on = models.DateField(default=timezone.now)

    def __str__(self):
            return f"{self.title} | {self.uploaded_by} | {self.uploaded_on}"
