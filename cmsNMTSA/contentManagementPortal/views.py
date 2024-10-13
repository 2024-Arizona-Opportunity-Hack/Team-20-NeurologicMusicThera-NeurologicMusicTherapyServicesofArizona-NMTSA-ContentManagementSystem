from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from accounts.models import UserProfile, CaregiverProfile
from .models import VideoContent, Article, Category, AccessGroup
from .serializers import VideosLoadSerializer, ArticleLoadSerializer
from django.shortcuts import render
import json
from django.contrib.auth.models import User
from contentManagementPortal.AI.textClassifierLlama3 import classify_text
from contentManagementPortal.AI.videoTranscriber import get_transcripts
from docx import Document
import PyPDF2
# Create your views here.

@api_view(["GET"])
def load_client_dashboard(request):
    user_groups = AccessGroup.objects.get(users=request.user.id)
    if user_groups.group_name == "consumer":
        profile = UserProfile.objects.get(user=request.user)
        videos = VideoContent.objects.filter(access_groups=user_groups.id, category=profile.treatment_category).order_by("-id")
        articles = Article.objects.filter(access_groups=user_groups.id, category=profile.treatment_category).order_by("-id")
    elif user_groups.group_name == "caregiver":
        linked_user = UserProfile.objects.get(caregivers=request.user.id)
        videos = VideoContent.objects.filter(access_groups=user_groups.id, category=linked_user.treatment_category).order_by("-id")
        articles = Article.objects.filter(access_groups=user_groups.id, category=linked_user.treatment_category).order_by("-id")
    else:
        videos = VideoContent.objects.filter(access_groups=user_groups.id).order_by("-id")
        articles = Article.objects.filter(access_groups=user_groups.id).order_by("-id")
    vid_serializer = VideosLoadSerializer(videos, many=True)
    article_serializer: ArticleLoadSerializer = ArticleLoadSerializer(articles, many=True)
    data = {
        'videos': vid_serializer.data,
        'articles': article_serializer.data
    }
    return Response(data, status=status.HTTP_200_OK)

@api_view(["GET"])
def load_admin_dashboard(request):
    videos = VideoContent.objects.all().order_by("-id")
    articles = Article.objects.all().order_by("-id")
    vid_serializer = VideosLoadSerializer(videos, many=True)
    article_serializer: ArticleLoadSerializer = ArticleLoadSerializer(articles, many=True)
    data = {
        'videos': vid_serializer.data,
        'articles': article_serializer.data,
        'users': [{'id': user.id, 'username': user.username, 'email': user.email} for user in User.objects.all()],
        'groups': list(AccessGroup.objects.values('id', 'group_name', 'users')),
        'categories': list(Category.objects.values('id', 'name'))
    }
    return Response(data, status=status.HTTP_200_OK)


@api_view(["PUT", "DELETE"])
@parser_classes([MultiPartParser, FormParser])
def update_video(request):
    if request.method == "DELETE":
        obj_id = json.loads(request.body).get("id")
        try:
            VideoContent.objects.get(id=obj_id).delete()
            return Response({"message":"video deleted"}, status=status.HTTP_204_NO_CONTENT)
        except VideoContent.DoesNotExist:
            return Response({"message":"video not found"}, status=status.HTTP_404_NOT_FOUND)

    else:
        data = json.loads(request.body)
        obj_id = data.get("id")
        try:
            vid = VideoContent.objects.get(id=obj_id)
            title = data.get("title")
            if title:
                vid.title = title
            category = data.get("category")
            if category:
                category = Category.objects.get(name=category)
                vid.category = category
            tags = data.get("tags")
            if tags:
                vid.tags = tags
            access_groups = data.get("access_groups")
            if access_groups:
                vid.access_groups.set(access_groups)
            vid.save()
            return Response({"message":"video updated"}, status=status.HTTP_200_OK)
        except VideoContent.DoesNotExist:
            return Response({"message": "video not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["PUT", "DELETE"])
@parser_classes([MultiPartParser, FormParser])
def update_article(request):
    if request.method == "DELETE":
        obj_id = json.loads(request.body).get("id")
        try:
            Article.objects.get(id=obj_id).delete()
            return Response({"message":"article deleted"}, status=status.HTTP_204_NO_CONTENT)
        except VideoContent.DoesNotExist:
            return Response({"message":"article not found"}, status=status.HTTP_404_NOT_FOUND)

    else:
        data = json.loads(request.body)
        obj_id = data.get("id")
        try:
            article = Article.objects.get(id=obj_id)
            title = data.get("title")
            if title:
                article.title = title
            category = data.get("category")
            if category:
                category = Category.objects.get(name=category)
                article.category = category
            tags = data.get("tags")
            if tags:
                article.tags = tags
            access_groups = data.get("access_groups")
            if access_groups:
                article.access_groups.set(access_groups)
            article.save()
            return Response({"message":"article updated"}, status=status.HTTP_200_OK)
        except VideoContent.DoesNotExist:
            return Response({"message": "article not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["PUT", "DELETE", "POST"])
def update_category(request):
    if request.method == "DELETE":
        cat_name = json.loads(request.body).get("category")
        try:
            Category.objects.get(name=cat_name).delete()
            return Response({"message": "category deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response({"message": "category not found"}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == "PUT":
        try:
            data = json.loads(request.body)
            obj_id = data.get("id")
            name = data.get("name")
            category = Category.objects.get(id=obj_id)
            category.name = name
            category.save()
            return Response({"message": "category edited"}, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({"message":"category not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
def create_category(request):
    data = json.loads(request.body)
    new_category = Category.objects.create(data.get("name"))
    new_category.save()
    return Response({"message": "category created"}, status=status.HTTP_200_OK)

@api_view(["POST", "GET"])
@parser_classes([MultiPartParser, FormParser])
def create_video(request):
    user_group = AccessGroup.objects.get(users=request.user).group_name
    if user_group == "admin" or user_group == "private":
        if request.method == "POST":
            form_data = json.loads(request.body)
            try:
                title = form_data.get('title')
                video = request.FILES.get('video')
                if not video:
                    return Response({"error": "No video file provided"}, status=status.HTTP_400_BAD_REQUEST)
                transcript = get_transcripts(video)
                llm_data = classify_text(transcript)
                category = Category.objects.get(name=llm_data.get("category"))
                tags = " ".join(llm_data.get("tags"))
                new_video = VideoContent.objects.create(title=title, video=video, transcript=transcript, upload_by=request.user, tags=tags)
                new_video.category.set(category)
                access_groups = ["admin"].extend(list(form_data.get('access_groups')))
                new_video.access_groups.set(access_groups)
                new_video.save()
                return Response(form_data, status=status.HTTP_201_CREATED)
            except Exception:
                return Response(json.dumps({"error":"Error in uploading video. Please retry"}), status=status.HTTP_400_BAD_REQUEST)
        else:
            return render(request, "create_video.html")
    return Response(json.dumps({"error": "You are not authorized!"}), status=status.HTTP_403_FORBIDDEN)

@api_view(["POST", "GET"])
@parser_classes([MultiPartParser, FormParser])
def create_article(request):
    user_group = AccessGroup.objects.get(users=request.user).group_name
    print(user_group)
    if user_group == "admin" or user_group == "private":
        if request.method == "POST":
            form_data = json.loads(request.body)
            try:
                title = form_data.get('title')
                article = request.FILES.get('article')
                if not article:
                    return Response({"error": "No article file provided"}, status=status.HTTP_400_BAD_REQUEST)
                ext = filename.split('.')[-1]
                if ext == "docx":
                    article_content = Document(article)
                elif ext == "pdf":
                    reader = PyPDF2.PdfFileReader(article)
                    num_pages = reader.numPages
                    article_content = " ".join([reader.getPage(page_num).extract_text() for page_num in range(num_pages)])
                content = " ".join([para.text for para in article_content.paragraphs])
                llm_data = classify_text(content)
                category = Category.objects.get(name=llm_data.get("category"))
                tags = " ".join(llm_data.get("tags"))
                new_article = Article.objects.create(title=title, article=article,
                                                        upload_by=request.user, tags=tags)
                new_article.category.set(category)
                access_groups = ["admin"].extend(list(form_data.get('access_groups')))
                new_article.access_groups.set(access_groups)
                new_article.save()
                return Response(form_data, status=status.HTTP_201_CREATED)
            except Exception:
                return Response(json.dumps({"error": "Error in uploading video. Please retry"}),
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return render(request, "create_video.html")
    return Response(json.dumps({"error": "You are not authorized!"}), status=status.HTTP_403_FORBIDDEN)

@api_view(["GET"])
def load_video(request):
    try:
        data = json.loads(request.body)
        user_group = AccessGroup.objects.users(request.user)
        vid = VideoContent.objects.get(id = data.get('id'), access_groups=user_group)
        return Response({"url": vid.video_file}, status=status.HTTP_200_OK)
    except VideoContent.DoesNotExist:
        return Response({"message":"video not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def load_article(request):
    try:
        data = json.loads(request.body)
        user_group = AccessGroup.objects.users(request.user)
        article = Article.objects.get(id = data.get('id'), access_groups=user_group)
        return Response({"url": article.article}, status=status.HTTP_200_OK)
    except VideoContent.DoesNotExist:
        return Response({"message":"article not found"}, status=status.HTTP_404_NOT_FOUND)
