import uuid
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import VideoContent, Article, Category, AccessGroup
from .serializers import VideosLoadSerializer, ArticleLoadSerializer
from django.shortcuts import render
import json
from django.contrib.auth.models import User, Group
from contentManagementPortal.AI.textClassifierLlama3 import classify_text
from contentManagementPortal.AI.videoTranscriber import get_transcripts
from docx import Document
import PyPDF2
# Create your views here.

@api_view(["GET"])
def load_client_dashboard(request):
    user_groups = AccessGroup.objects.get(users=request.user.id)
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
        'groups': list(AccessGroup.objects.values('id', 'group_name'))
    }
    return Response(data, status=status.HTTP_200_OK)


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