from django.urls import path
from users import views
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

urlpatterns = [
    path("admin/login/", LoginView.as_view(template_name="users/auth/login.html")),
    path("login/", LoginView.as_view(template_name="users/auth/login.html")),
    path("logout/", LogoutView.as_view(template_name="users/auth/logout.html")),
    path(
        "password_change/",
        PasswordChangeView.as_view(template_name="users/auth/password_change.html"),
    ),
    path(
        "password_change/done/",
        PasswordChangeDoneView.as_view(template_name="users/auth/password_change_done.html"),
    ),
    path(
        "password_reset/",
        PasswordResetView.as_view(template_name="users/auth/password_reset.html"),
        name='password_reset'
    ),
    path(
        "password_reset/done/",
        PasswordResetDoneView.as_view(template_name="users/auth/password_reset_done.html"),
    ),
    path(
        "reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="users/auth/password_reset_confirm.html"
        ),
    ),
    path(
        "reset/done/",
        PasswordResetCompleteView.as_view(
            template_name="users/auth/password_reset_complete.html"
        ),
    ),
    path('signup/', views.SignupView.as_view(), name='sign_up'),
]
