from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        'Почта',
        unique=True
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(
        'Аватарка',
        upload_to='uploads/',
        null=True
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
    mobile = models.PositiveIntegerField(
        'Номер телефона',
        null=True
    )
    description = models.TextField(
        'Описание',
        null=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
