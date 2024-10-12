from rest_framework.serializers import ModelSerializer
from .models import VideoContent, Article, Category

class VideosLoadSerializer(ModelSerializer):
    class Meta:
       model = VideoContent
       fields = "__all__"
       read_only_fields = []

    '''def create(self, validated_data):
        print("Validated data:", validated_data)  # Add this line to log validated data
        video = VideoContent.objects.create()
        #VideoContent.category.add(validated_data["users"])
        video.save()
        return video'''

class ArticleLoadSerializer(ModelSerializer):
    class Meta:
       model = Article
       fields = "__all__"
       read_only_fields = []

    '''def create(self, validated_data):
        print("Validated data:", validated_data)  # Add this line to log validated data
        video = VideoContent.objects.create()
        #VideoContent.category.add(validated_data["users"])
        video.save()
        return video'''