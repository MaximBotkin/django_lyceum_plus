# Generated by Django 3.2.13 on 2022-05-04 16:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customuser",
            options={
                "verbose_name": "пользователь",
                "verbose_name_plural": "пользователи",
            },
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        default="user", max_length=50, verbose_name="Никнэйм"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=50, null=True, verbose_name="Имя"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=50, null=True, verbose_name="Фамилия"),
                ),
                ("description", models.TextField(null=True, verbose_name="Описание")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
