from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from .managers import CustomUserManager
from sorl.thumbnail import get_thumbnail
from django.urls import reverse
from .validators import validate_for_username, validate_for_mobile


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        'Почта',
        unique=True
    )
    is_staff = models.BooleanField(
        default=False
    )
    is_active = models.BooleanField(
        default=True
    )
    date_joined = models.DateTimeField(
        default=timezone.now
    )
    avatar = models.ImageField(
        'Аватарка',
        upload_to='uploads/',
        null=True,
        blank=True
    )
    username = models.CharField(
        'Никнэйм',
        max_length=50,
        unique=True,
        validators=[validate_for_username]
    )
    first_name = models.CharField(
        'Имя',
        max_length=50,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=50,
        null=True,
        blank=True
    )
    birthday = models.DateField(
        'Дата рождения',
        null=True,
        blank=True
    )
    mobile = models.PositiveIntegerField(
        'Номер телефона',
        null=True,
        blank=True,
        validators=[validate_for_mobile]
    )
    description = models.TextField(
        'Описание',
        null=True,
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_image_400x400(self):
        return get_thumbnail(self.avatar, '400x400', crop='center', quality=60)

    def get_image_100x100(self):
        return get_thumbnail(self.avatar, '100x100', crop='center', quality=60)

    def get_full_name(self):
        return f'{str(self.first_name).capitalize()} {str(self.last_name).capitalize()}'

    def get_absolute_url(self):
        return reverse("users:user_detail", kwargs={"username": self.username})

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Subscription(models.Model):
    person = models.ForeignKey(
        'CustomUser',
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='person_who_has_subscribers'
    )
    subscriber = models.ForeignKey(
        'CustomUser',
        verbose_name='Подписчик',
        on_delete=models.CASCADE,
        related_name='subscribers',
    )
    is_subscribed = models.BooleanField(
        'Подписка активна',
        default=True,
    )

    def __str__(self):
        return f'{self.subscriber} подписался на {self.person}'

    class Meta:
        unique_together = ['person', 'subscriber']
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
