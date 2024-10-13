from django.db import models
from django.contrib.auth.models import User
import uuid, os
from contentManagementPortal.models import AccessGroup, Category
# Create your models here.

def generate_new_filename(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f"{uuid.uuid4().hex}.{ext}"
    return os.path.join('user_data/profile_pics', new_filename)

class CaregiverProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to=generate_new_filename)

    def __str__(self):
        return self.user.username

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to=generate_new_filename)
    treatment_category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)
    caregivers = models.ManyToManyField(CaregiverProfile)

    def __str__(self):
        return self.user.username
