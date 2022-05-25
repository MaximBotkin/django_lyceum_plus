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
from django.core.files.images import get_image_dimensions


User = get_user_model()


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
    creation_date = models.DateTimeField("Дата создания", auto_now=True, editable=False)
    votes = GenericRelation(LikeDislike, related_query_name="posts")
    tags = TaggableManager(through=TaggedWhatever)

    def __str__(self):
        return self.title[:30]

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"

    def get_absolute_url(self):
        return reverse("posts:postdetail", kwargs={"id": self.pk})

    objects = PostManager()


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(
        verbose_name="Изображение",
        upload_to="uploads/",
    )

    def get_image(self, img_width, img_height):
        width, height = get_image_dimensions(self.image.file)
        resize = min(width / img_width, height / img_height)
        return get_thumbnail(self.image, f"{int(resize * width)}x{int(resize * height)}", crop="center", quality=100)

    def get_image_1200x1200(self):
        return self.get_image(1200, 1200)

    def image_tmb(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="50">')
        return "Изображение отсутствует"

    image_tmb.short_description = "Превью"
    image_tmb.allow_tags = True

    class Meta:
        verbose_name = "Фотография, связанная с постом"
        verbose_name_plural = "Фотографии, связанные с постом"

    def __str__(self):
        return self.post.title
