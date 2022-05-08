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
    pass
