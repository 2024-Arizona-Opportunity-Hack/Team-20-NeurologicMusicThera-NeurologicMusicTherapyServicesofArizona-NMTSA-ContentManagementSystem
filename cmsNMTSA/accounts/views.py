from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
import json
from django.contrib.auth.models import User
from .models import UserProfile
from contentManagementPortal.models import AccessGroup
from rest_framework.response import Response
from django.middleware.csrf import get_token
from django.http import JsonResponse


# Create your views here.

@api_view(["GET", "POST"])
def login_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username = username, password=password)

        if user is not None:
            login(request, user)
            return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
        else:
            return Response({"error":"Invalid credentials"}, status=status.HTTP_403_FORBIDDEN)
    else:
        return render(request, "login.html")


@api_view(["GET", "POST"])
@parser_classes([MultiPartParser, FormParser])
def register_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        profile_pic = request.FILES.get('profile_pic')

        new_user = User.objects.create(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
        new_user.save()

        profile = UserProfile.objects.create(user=new_user)
        profile.profile_pic = profile_pic
        profile.save()
        if data.get("role") == "consumer":
            access_group = AccessGroup.objects.get(name="consumer")
        elif data.get("role") == "caregiver":
            access_group = AccessGroup.objects.get(name="caregiver")
        access_group.users.add(new_user)
        access_group.save()

        login(request, new_user)
        return Response({"message":"registration complete"}, status.HTTP_200_OK)

    else:
        return render(request, "sign_up.html")

@api_view(["GET"])
def user_logout(request):
    if request.user.is_authenticated:
        logout(request.user)
    return Response({"message":"user logged out"}, status=status.HTTP_200_OK)


def load_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})