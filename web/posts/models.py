
from django.db import models
from django.contrib.auth import get_user_model
from description.models import Category, Tag
from posts.managers import PostManager

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=64, default='title', verbose_name='Заголовок')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', null=True)
    text = models.TextField(max_length=200, default='text', verbose_name='Текст')
    tags = models.ManyToManyField(Tag, verbose_name='Тэги', blank=True)
    creation_date = models.DateTimeField('Дата создания', auto_now=True, editable=False)

    def __str__(self):
        return self.title[:30]

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    objects = PostManager()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', null=True)

    class Meta:
        verbose_name = 'Комментрий'
        verbose_name_plural = 'Комментрии'


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
