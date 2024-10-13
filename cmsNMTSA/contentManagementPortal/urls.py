from django.urls import path, include
from .views import *

app_name = "contentManagementPortal"

urlpatterns = [
    path('dashboard/user', load_client_dashboard , name="loadClientDashboard"),
    path('dashboard/admin', load_admin_dashboard , name="loadAdminDashboard"),
    path('dashboard/create/video', create_video, name="createVideo"),
    path('dashboard/create/article', create_article, name="createArticle"),
    path('videos/view', load_video, name="view_video"),
    path('articles/read', load_article, name="read_article"),
    path('dashboard/edit/video', update_video, name="update_video"),
    path('dashboard/edit/article', update_article, name="update_article"),
    path('dashboard/edit/category', update_category, name="update_category"),
    path('dashboard/create/category', create_category, name="create_category"),
]