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
    path(
        "login/", LoginView.as_view(template_name="users/auth/login.html"), name="login"
    ),
    path(
        "logout/", LogoutView.as_view(template_name="users/auth/logout.html"), name='logout'
    ),
    path(
        "password_change/",
        PasswordChangeView.as_view(template_name="users/auth/password_change.html"),
        name='password_change'
    ),
    path(
        "password_change/done/",
        PasswordChangeDoneView.as_view(
            template_name="users/auth/password_change_done.html"
        ),
        name='password_change_done'
    ),
    path(
        "password_reset/",
        PasswordResetView.as_view(template_name="users/auth/password_reset.html"),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        PasswordResetDoneView.as_view(
            template_name="users/auth/password_reset_done.html"
        ),
        name='password_reset_done'
    ),
    path(
        "reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="users/auth/password_reset_confirm.html"
        ),
        name='password_reset_confirm',
    ),
    path(
        "reset/done/",
        PasswordResetCompleteView.as_view(
            template_name="users/auth/password_reset_complete.html"
        ),
        name='password_reset_complete',
    ),
    path(
        "signup/", views.SignupView.as_view(), name="sign_up"
    ),
]
