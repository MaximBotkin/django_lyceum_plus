from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from .models import LikeDislike
from posts.models import Post


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
        name="check_estimated"
    )
]
