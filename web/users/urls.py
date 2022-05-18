from django.urls import path
from .views import (
    UserListView,
    UserDetailView,
    ProfileView,
    validate_username,
    validate_email,
)


app_name = "users"


urlpatterns = [
    path("", UserListView.as_view(), name="user_list"),
    path("<username>/", UserDetailView.as_view(), name="user_detail"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("validate_username", validate_username, name="validate_username"),
    path("validate_email", validate_email, name="validate_email"),
]
