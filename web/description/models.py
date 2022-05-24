from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from colorfield.fields import ColorField
import description.managers as managers
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from taggit.models import TagBase, GenericTaggedItemBase
from django.utils.http import urlencode


User = get_user_model()


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTES = ((DISLIKE, "Не нравится"), (LIKE, "Нравится"))

    vote = models.SmallIntegerField(verbose_name=("Голос"), choices=VOTES)
    user = models.ForeignKey(
        User, verbose_name=("Пользователь"), on_delete=models.CASCADE
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"

    def __str__(self) -> str:
        return "Дизлайк" if self.vote == -1 else "Лайк"

    objects = managers.LikeDislikeManager()


class Category(models.Model):
    name = models.CharField("Название", max_length=50, unique=True)
    color = ColorField(default="#FFFFFF", format="hex")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def get_absolute_url(self):
        return reverse("categories:category", kwargs={"category_id": self.pk})

    def __str__(self):
        return self.name[:30]

    objects = managers.CategoryManager()


class Tag(TagBase):
    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def get_absolute_filter_url(self):
        return "%s?%s" % (
            reverse("homepage:home"),
            urlencode({"tag_filter": self.slug}),
        )


class TaggedWhatever(GenericTaggedItemBase):
    # TaggedWhatever can also extend TaggedItemBase or a combination of
    # both TaggedItemBase and GenericTaggedItemBase. GenericTaggedItemBase
    # allows using the same tag for different kinds of objects, in this
    # example Food and Drink.

    # Here is where you provide your custom Tag class.
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_items",
    )
