from email.headerregistry import Group
from rest_framework.response import Response
from rest_framework.decorators import api_view
from sympy.integrals.meijerint_doc import category

from .models import VideoContent, Article, Category, AccessGroup
from .serializers import VideosLoadSerializer, ArticleLoadSerializer
from itertools import chain
# Create your views here.

@api_view(["GET"])
def load_client_dashboard(request):
    user_groups = Group.objects.get(users=request.user.id)
    videos = VideoContent.objects.filter(access_groups=user_groups.id)
    articles = Article.objects.filter(access_groups=user_groups.id)
    vid_serializer = VideosLoadSerializer(videos, many=True)
    article_serializer: ArticleLoadSerializer = ArticleLoadSerializer(articles, many=True)
    data = {
        'videos': vid_serializer.data,
        'articles': article_serializer.data
    }
    return Response(data)

def load_admin_dashboard(request):
    videos = VideoContent.objects.all()
    articles = VideoContent.objects.all()
    vid_serializer = VideosLoadSerializer(videos, many=True)
    article_serializer: ArticleLoadSerializer = ArticleLoadSerializer(articles, many=True)
    data = {
        'videos': vid_serializer.data,
        'articles': article_serializer.data
    }
    return Response(data)

def search_content(request, query):
    group = AccessGroup.objects.get(users=request.user)

    if group.group_name == "admin":
        videos = list(chain(VideoContent.objects.filter(tags__icontains=query), VideoContent.objects.filter(category__name__icontains=query)))




@api_view(["POST"])
def create_video(request):
    serializer = VideoLoadSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def create_article(request):
    serializer = ArticleLoadSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
=
