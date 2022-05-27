# Generated by Django 3.2.13 on 2022-05-05 20:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("description", "0003_alter_category_color"),
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="description.category",
                verbose_name="Категории",
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(to="description.Tag", verbose_name="Тэги"),
        ),
        migrations.AddField(
            model_name="post",
            name="text",
            field=models.TextField(default="text", max_length=200),
        ),
        migrations.AddField(
            model_name="post",
            name="title",
            field=models.TextField(default="title", max_length=64),
        ),
    ]
