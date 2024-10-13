from django.contrib import admin
from .models import UserProfile, CaregiverProfile
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(CaregiverProfile)