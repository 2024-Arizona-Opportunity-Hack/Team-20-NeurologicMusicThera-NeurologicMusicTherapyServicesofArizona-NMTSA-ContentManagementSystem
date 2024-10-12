from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import VideoContent, Article, Category, AccessGroup
from .serializers import VideosLoadSerializer, ArticleLoadSerializer
# Create your views here.

@api_view(["GET"])
def fetch_promo_videos(request):
    public_group = AccessGroup.objects.get(name="public")
    videos = VideoContent.objects.filter(access_groups=public_group.id)
    serializer = VideosLoadSerializer(videos, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def fetch_consumer_videos(request):
    group = AccessGroup.objects.get(name="consumer")
    videos = VideoContent.objects.filter(access_groups=group.id)
    serializer = VideosLoadSerializer(videos, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def fetch_caregiver_videos(request):
    group = AccessGroup.objects.get(name="caregivers")
    videos = VideoContent.objects.filter(access_groups=group.id)
    serializer = VideosLoadSerializer(videos, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def fetch_private_videos(request):
    group = AccessGroup.objects.get(name="private")
    videos = VideoContent.objects.filter(access_groups=group.id)
    serializer = VideosLoadSerializer(videos, many=True)
    return Response(serializer.data)



@api_view(["GET"])
def fetch_promo_articles(request):
    public_group = AccessGroup.objects.get(name="public")
    videos = Article.objects.filter(access_groups=public_group.id)
    serializer = ArticleLoadSerializer(videos, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def fetch_consumer_articles(request):
    group = AccessGroup.objects.get(name="consumer")
    videos = Article.objects.filter(access_groups=group.id)
    serializer = ArticleLoadSerializer(videos, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def fetch_caregiver_articles(request):
    group = AccessGroup.objects.get(name="caregivers")
    videos = Article.objects.filter(access_groups=group.id)
    serializer = ArticleLoadSerializer(videos, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def fetch_private_articles(request):
    group = AccessGroup.objects.get(name="private")
    videos = Article.objects.filter(access_groups=group.id)
    serializer = ArticleLoadSerializer(videos, many=True)
    return Response(serializer.data)
