import uuid
from email.headerregistry import Group
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
# Create your views here.

@api_view(["GET"])
def load_client_dashboard(request):
    user_groups = Group.objects.get(users=request.user.id)
    videos = VideoContent.objects.filter(access_groups=user_groups.id).order_by["-id"]
    articles = Article.objects.filter(access_groups=user_groups.id).order_by["-id"]
    vid_serializer = VideosLoadSerializer(videos, many=True)
    article_serializer: ArticleLoadSerializer = ArticleLoadSerializer(articles, many=True)
    data = {
        'videos': vid_serializer.data,
        'articles': article_serializer.data
    }
    return Response(data, status=status.HTTP_200_OK)

@api_view(["GET"])
def load_admin_dashboard(request):
    videos = VideoContent.objects.all().order_by["-id"]
    articles = Article.objects.all().order_by["-id"]
    vid_serializer = VideosLoadSerializer(videos, many=True)
    article_serializer: ArticleLoadSerializer = ArticleLoadSerializer(articles, many=True)
    data = {
        'videos': vid_serializer.data,
        'articles': article_serializer.data,
        'users': User.objects.all(),
        'groups': Group.objects.all()
    }
    return Response(data, status=status.HTTP_200_OK)

'''def search_content(request, query):
    group = AccessGroup.objects.get(users=request.user)

    if group.group_name == "admin":
        videos = list(chain(VideoContent.objects.filter(title=query), VideoContent.objects.filter(tags__icontains=query), VideoContent.objects.filter(category__name__icontains=query)))
        articles = list(chain(Article.objects.filter(title=query), Article.objects.filter(tags__icontains=query), Article.objects.filter(category__name__icontains=query)))

    else:
        group = Group.objects.get(users=request.user)
        videos = list(
            chain(VideoContent.objects.filter(title=query, access_groups=group), VideoContent.objects.filter(tags__icontains=query, access_groups=group),
                  VideoContent.objects.filter(category__name__icontains=query, access_groups=group)))
        articles = list(chain(Article.objects.filter(title=query, access_groups=group), Article.objects.filter(tags__icontains=query, access_groups=group),
                              Article.objects.filter(category__name__icontains=query, access_groups=group)))

    vid_serializer = VideosLoadSerializer(videos, many=True)
    article_serializer: ArticleLoadSerializer = ArticleLoadSerializer(articles, many=True)
    data = {
        'videos': vid_serializer.data,
        'articles': article_serializer.data
    }
    return Response(data)


def filter_content(request, query):'''


@api_view(["POST", "GET"])
@parser_classes([MultiPartParser, FormParser])
def create_video(request):
    user_group = Group.objects.get(users=request.user)
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
    user_group = Group.objects.get(users=request.user)
    if user_group == "admin" or user_group == "private":
        if request.method == "POST":
            form_data = json.loads(request.body)
            try:
                title = form_data.get('title')
                article = request.FILES.get('article')
                if not article:
                    return Response({"error": "No article file provided"}, status=status.HTTP_400_BAD_REQUEST)
                article_content = Document(article)
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
