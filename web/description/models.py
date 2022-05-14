from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from colorfield.fields import ColorField
import description.managers as managers


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
        'posts.Post', on_delete=models.CASCADE, related_name=AbstractRating.RELATED_NAME
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
    color = ColorField(default='#FFFFFF', format='hex')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def get_absolute_url(self):
        return reverse("categories:category", kwargs={"category_id": self.pk})

    def __str__(self):
        return self.name[:30]

    objects = managers.CategoryManager()
