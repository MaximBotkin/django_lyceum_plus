# Generated by Django 3.2.13 on 2022-05-08 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20220506_1634'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Публикация', 'verbose_name_plural': 'Публикации'},
        ),
        migrations.AddField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата создания'),
        ),
    ]