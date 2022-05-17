from django.db import models
from django.contrib.auth import get_user_model
from description.models import Category, Tag
from posts.managers import PostManager
from sorl.thumbnail import get_thumbnail
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField
from django.urls import reverse


User = get_user_model()


class PostImage(models.Model):
    post = models.ForeignKey('Post', verbose_name='Товар', default=None, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Изображение', upload_to='uploads/')

    def get_image_400x300(self):
        return get_thumbnail(self.image, '400x300', crop='center', quality=60)

    class Meta:
        verbose_name = "Фотография, связанная с постом"
        verbose_name_plural = "Фотографии, связанные с постом"

    def __str__(self):
        return self.post.title


class Post(models.Model):
    title = models.CharField(max_length=64, default='title', verbose_name='Заголовок')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория',
                                 null=True, related_name='posts')
    text = RichTextField(verbose_name='Текст', null=False)
    tags = models.ManyToManyField(Tag, verbose_name='Тэги', blank=True)
    upload = models.ImageField('Главное изображение', upload_to='uploads/', null=True)
    creation_date = models.DateTimeField('Дата создания', auto_now=True, editable=False)

    def get_image_300x300(self):
        if self.upload:
            return get_thumbnail(self.upload, '300x300', crop='center', quality=100)

    def image_tmb(self):
        if self.upload:
            return mark_safe(f'<img src="{self.upload.url}" width="50">')
        return 'Изображение отсутствует'

    image_tmb.short_description = 'Превью'
    image_tmb.allow_tags = True

    def __str__(self):
        return self.title[:30]

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def get_absolute_url(self):
        return reverse("posts:postdetail", kwargs={"id": self.pk})

    objects = PostManager()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', null=True)
    text = RichTextField(verbose_name='Текст', null=False, default='')
    creation_date = models.DateTimeField('Дата создания', auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class PostComment(Comment):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Публикация', related_name='comments')

    class Meta:
        verbose_name = 'Комментарий к публикации'
        verbose_name_plural = 'Комментарии к публикациям'


class UserComment(Comment):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='comments')

    class Meta:
        verbose_name = 'Комментарий к пользователю'
        verbose_name_plural = 'Комментарии к пользователям'


class ReplyComment(Comment):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name='Комментарий', related_name='comments')

    class Meta:
        verbose_name = 'Ответ на комментарий'
        verbose_name_plural = 'Ответы на комментарии'
