from django.db import models
from django.contrib.auth import get_user_model
from description.models import Category, Tag

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=64, default='title', verbose_name='Заголовок')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', null=True)
    text = models.TextField(max_length=200, default='text', verbose_name='Текст')
    tags = models.ManyToManyField(Tag, verbose_name='Тэги', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'посты'


class Comment(models.Model):
    pass
