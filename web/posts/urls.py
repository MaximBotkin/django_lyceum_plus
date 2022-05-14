from django.urls import path
from .views import PostsView, CreatePostView, PostDetailView


app_name = "posts"


urlpatterns = [
    path("", PostsView.as_view(), name="home"),
    path("posts/newpost/", CreatePostView.as_view(), name="newpost"),
    path("posts/<int:id>/", PostDetailView.as_view(), name="postdetail")
]
