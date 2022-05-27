from django.urls import path

from .views import (ProfileView, UserDetailView, UserListView, validate_email,
                    validate_username)

app_name = "users"


urlpatterns = [
    path("", UserListView.as_view(), name="user_list"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("<username>/", UserDetailView.as_view(), name="user_detail"),
    path("validate_username", validate_username, name="validate_username"),
    path("validate_email", validate_email, name="validate_email"),
]
