from django.urls import path
from .views import CreatePostView, PostDetailView


app_name = "posts"


urlpatterns = [
    path("newpost/", CreatePostView.as_view(), name="newpost"),
    path("<int:id>/", PostDetailView.as_view(), name="postdetail"),
]
