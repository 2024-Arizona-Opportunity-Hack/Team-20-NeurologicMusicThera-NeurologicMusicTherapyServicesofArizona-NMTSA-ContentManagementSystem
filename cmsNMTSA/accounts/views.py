from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
import json
from django.contrib.auth.models import User
from .models import UserProfile, CaregiverProfile
from contentManagementPortal.models import AccessGroup
from rest_framework.response import Response
from django.middleware.csrf import get_token
from django.http import JsonResponse
from contentManagementPortal.models import AccessGroup


# Create your views here.

@api_view(["POST"])
def login_user(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')

    user = authenticate(username = username, password=password)

    if user is not None:
        login(request, user)
        access_group = AccessGroup.objects.get(users=user.id)
        if access_group.group_name == "admin":
            return redirect("http://localhost:3000/web/dashboard/admin")
        return redirect("http://localhost:3000/web/dashboard/users")
    else:
        return Response({"error":"Invalid credentials"}, status=status.HTTP_403_FORBIDDEN)


@api_view(["POST"])
@parser_classes([MultiPartParser, FormParser])
def register_user(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    profile_pic = request.FILES.get('profile_pic')
    new_user = User.objects.create(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
    new_user.save()
    treatment_category = data.get("category")
    access_group = AccessGroup.objects.get(name="consumer")
    profile = UserProfile.objects.create(user=new_user, treatment_category= treatment_category)
    profile.profile_pic = profile_pic
    profile.save()
    access_group.users.add(new_user)
    access_group.save()
    login(request, new_user)
    return redirect("http://localhost:3000/web/dashboard/user")

@api_view(["GET"])
def user_logout(request):
    if request.user.is_authenticated:
        logout(request.user)
    return redirect("http://localhost:3000/")


def load_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})

@api_view(["POST"])
def add_caregiver(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    profile_pic = request.FILES.get('profile_pic')
    new_user = User.objects.create(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
    new_user.save()
    access_group = AccessGroup.objects.get(name="caregiver")
    profile = CaregiverProfile.objects.create(user=new_user)
    profile.profile_pic = profile_pic
    profile.save()
    access_group.users.add(new_user)
    access_group.save()
    user_profile = UserProfile.objects.get(user=request.user)
    user_profile.caregivers.add(profile)
    return redirect("http://localhost:3000/web/dashboard/user")