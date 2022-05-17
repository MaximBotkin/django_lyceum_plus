# Generated by Django 3.2.13 on 2022-05-17 12:16

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_alter_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='creation_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Текст'),
        ),
    ]
