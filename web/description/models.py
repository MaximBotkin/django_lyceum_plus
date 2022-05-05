from django.db import models
from django.contrib.auth import get_user_model
from posts.models import Post
from description.validators import RegexValidator


User = get_user_model()


class AbstractRating(models.Model):
    RELATED_NAME = "rating"
    CHOICES = (
        (1, "Лайк"),
        (0, "Нейтрально"),
        (-1, "Дизлайк"),
    )
    star = models.IntegerField("Оценка", choices=CHOICES, default=CHOICES[1][0])
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name=RELATED_NAME)

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class PostRating(AbstractRating):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name=AbstractRating.RELATED_NAME
    )

    class Meta:
        verbose_name = "Рейтинг публикации"
        verbose_name_plural = "Рейтинги публикаций"

    def __str__(self):
        return str(self.star)


class Tag(models.Model):
    name = models.CharField("Название", max_length=50, unique=True)
    slug = models.SlugField("Slug", unique=True, max_length=300)

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return self.name[:30]


class Category(models.Model):
    name = models.CharField("Название", max_length=50, unique=True)
    color = models.CharField(
        "Цвет",
        default="#FFF",
        max_length=9,
        validators=[RegexValidator("#([a-zA-Z0-9]{8}|[a-zA-Z0-9]{6}|[a-zA-Z0-9]{3})")],
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name[:30]
