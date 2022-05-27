from django.contrib.auth.decorators import login_required
from django.urls import path
from posts.models import Post

from . import views
from .models import LikeDislike

app_name = "estimation"


urlpatterns = [
    path(
        "posts/like/",
        login_required(views.VotesView.as_view(model=Post, vote_type=LikeDislike.LIKE)),
        name="post_like",
    ),
    path(
        "posts/dislike/",
        login_required(
            views.VotesView.as_view(model=Post, vote_type=LikeDislike.DISLIKE)
        ),
        name="post_dislike",
    ),
    path(
        "posts/check_estimated/",
        views.CheckEstimatedView.as_view(model=Post),
        name="check_estimated",
    ),
]
