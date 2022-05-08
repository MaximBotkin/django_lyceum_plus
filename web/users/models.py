from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from .managers import CustomUserManager
from sorl.thumbnail import get_thumbnail
from django.urls import reverse


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
    birthday = models.DateField(
        'Дата рождения',
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

    def get_image_400x300(self):
        return get_thumbnail(self.avatar, '400x300', crop='center', quality=60)

    def get_full_name(self):
        return f'{str(self.first_name).capitalize()} {str(self.last_name).capitalize()}'

    def get_absolute_url(self):
        return reverse("users:user_detail", kwargs={"user_id": self.pk})

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
