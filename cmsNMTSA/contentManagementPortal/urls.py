from django.urls import path, include
from .views import *

urlpatterns = [
    path('dashboard/consumer', fetch_consumer_videos, name="getConsumerVideos"),
    path('dashboard/caregiver', fetch_caregiver_videos, name="getCareGiverVideos"),
    path('dashboard/admin', )
    path('cms/', include(contentManagementPortal.urls)),

]