from django.urls import path
from .views import PostsView, CreatePostView


app_name = "posts"


urlpatterns = [
    path("", PostsView.as_view(), name="home"),
    path("newpost", CreatePostView.as_view(), name="newpost"),
]
