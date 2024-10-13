from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user , name="login_user"),
    path('register/', views.register_user , name="user_register"),
    path('logout/', views.user_logout, name="user_logout"),
    path('api/csrf', views.load_csrf_token, name="load_csrf_token")
]