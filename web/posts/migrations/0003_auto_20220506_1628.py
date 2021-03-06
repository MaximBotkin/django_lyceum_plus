# Generated by Django 3.2.13 on 2022-05-06 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("description", "0003_alter_category_color"),
        ("posts", "0002_auto_20220505_2323"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"verbose_name": "Пост", "verbose_name_plural": "посты"},
        ),
        migrations.AlterField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(
                blank=True, to="description.Tag", verbose_name="Тэги"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="text",
            field=models.TextField(
                default="text", max_length=200, verbose_name="Текст"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.TextField(
                default="title", max_length=64, verbose_name="Заголовок"
            ),
        ),
    ]
