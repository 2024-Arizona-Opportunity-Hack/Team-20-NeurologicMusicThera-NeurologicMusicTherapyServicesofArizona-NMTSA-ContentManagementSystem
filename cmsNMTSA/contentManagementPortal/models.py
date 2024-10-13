from django.db import models
from django.db.models import ManyToManyField
from django.contrib.auth.models import User, Group
from django.utils import timezone
import uuid, os
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

class AccessGroup(models.Model):
    group_name = models.CharField(max_length=400)
    users = ManyToManyField(User)

def generate_new_filename(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f"{uuid.uuid4().hex}.{ext}"
    return os.path.join('content/videos', new_filename)

class VideoContent(models.Model):
    title = models.CharField(max_length=400)
    video_file = models.FileField(upload_to=generate_new_filename)
    transcript = models.TextField(default="No transcript available")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    access_groups = models.ManyToManyField(AccessGroup)
    uploaded_by = models.ForeignKey(User, on_delete=models.PROTECT)
    uploaded_on = models.DateField(default=timezone.now)

class Article(models.Model):
    title = models.CharField(max_length=400)
    article = models.FileField(upload_to=generate_new_filename)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    access_groups = models.ManyToManyField(AccessGroup)
    uploaded_by = models.ForeignKey(User, on_delete=models.PROTECT)
    uploaded_on = models.DateField(default=timezone.now)

