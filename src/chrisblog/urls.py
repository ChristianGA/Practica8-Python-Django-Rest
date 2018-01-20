"""chrisblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from posts.api import BlogsListAPI, PostDetailUpdateDeleteAPI, PostListAPI, PostCreateAPI
from posts.views import NewPostView, MyPostsView, BlogsListView, HomeView, PostDetailView
from users.api import UserDetailUpdateDeleteAPI, UserCreateAPI
from users.views import logout, loginView, signupView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', loginView.as_view(), name = "login_page"),
    path('logout/', logout, name = "logout_page"),
    path('blogs/<str:username>/<int:pk>', PostDetailView.as_view(), name = "post_detail_page"),
    path('blogs/<str:username>/', MyPostsView.as_view(), name = "post_detail"),
    path('blogs/', BlogsListView.as_view(), name = "blogslist"),
    path('new-post/', NewPostView.as_view(), name = "newpost_page"),
    path('signup/', signupView.as_view(), name = "signup_page"),
    path('', HomeView.as_view(), name = "home_page"),

    # API REST

    path('api/1.0/users/<int:pk>/', UserDetailUpdateDeleteAPI.as_view(), name = "api_user_detailcreatedelete"),
    path('api/1.0/users/', UserCreateAPI.as_view(), name = "api_user_creation"),

    path('api/1.0/blogs/', BlogsListAPI.as_view(), name = "api_blogs_list"),

    path('api/1.0/posts/<str:username>/<int:pk>/', PostDetailUpdateDeleteAPI.as_view(), name = "api_post_detailcreatedelete"),
    path('api/1.0/posts/<str:username>/', PostListAPI.as_view(), name = "api_post_list"),
    path('api/1.0/posts/', PostCreateAPI.as_view(), name = "api_post_creation")

]
