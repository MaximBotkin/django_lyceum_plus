from django.db import models
from django.contrib.auth import get_user_model
from description.models import Category
from posts.managers import PostManager
from sorl.thumbnail import get_thumbnail
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField
from django.urls import reverse
from description.models import LikeDislike
from django.contrib.contenttypes.fields import GenericRelation
from taggit.managers import TaggableManager
from description.models import TaggedWhatever


User = get_user_model()


class PostImage(models.Model):
    post = models.ForeignKey(
        "Post", verbose_name="Товар", default=None, on_delete=models.CASCADE
    )
    image = models.ImageField(verbose_name="Изображение", upload_to="uploads/")

    def get_image_400x300(self):
        return get_thumbnail(self.image, "400x300", crop="center", quality=60)

    class Meta:
        verbose_name = "Фотография, связанная с постом"
        verbose_name_plural = "Фотографии, связанные с постом"

    def __str__(self):
        return self.post.title


class Post(models.Model):
    title = models.CharField(max_length=64, default="title", verbose_name="Заголовок")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, verbose_name="Автор"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        null=True,
        related_name="posts",
    )
    text = RichTextField(verbose_name="Текст", null=False)
    upload = models.ImageField("Главное изображение", upload_to="uploads/", null=True)
    creation_date = models.DateTimeField("Дата создания", auto_now=True, editable=False)
    votes = GenericRelation(LikeDislike, related_query_name="posts")
    tags = TaggableManager(through=TaggedWhatever)

    def get_image_300x300(self):
        if self.upload:
            return get_thumbnail(self.upload, "300x300", crop="center", quality=100)

    def image_tmb(self):
        if self.upload:
            return mark_safe(f'<img src="{self.upload.url}" width="50">')
        return "Изображение отсутствует"

    image_tmb.short_description = "Превью"
    image_tmb.allow_tags = True

    def __str__(self):
        return self.title[:30]

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"

    def get_absolute_url(self):
        return reverse("posts:postdetail", kwargs={"id": self.pk})

    objects = PostManager()
