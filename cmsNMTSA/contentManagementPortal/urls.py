from django.urls import path, include
from .views import *

app_name = "contentManagementPortal"

urlpatterns = [
    path('dashboard/user', load_client_dashboard , name="loadClientDashboard"),
    path('dashboard/admin', load_admin_dashboard , name="loadAdminDashboard"),
    path('dashboard/create/video', create_video, name="createVideo"),
    path('dashboard/create/article', create_article, name="createArticle"),
]