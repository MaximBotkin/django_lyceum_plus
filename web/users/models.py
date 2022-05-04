from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from .managers import CustomUserManager
from web import settings


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Profile(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    username = models.CharField(
        'Никнэйм',
        max_length=50,
        default='user'
    )
    first_name = models.CharField(
        'Имя',
        max_length=50,
        null=True
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=50,
        null=True
    )
    description = models.TextField(
        'Описание',
        null=True
    )

    def __str__(self):
        return self.email
