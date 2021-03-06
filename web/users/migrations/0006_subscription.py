# Generated by Django 3.2.13 on 2022-05-11 08:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_customuser_birthday"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subscription",
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
                    "is_subscribed",
                    models.BooleanField(default=True, verbose_name="Подписка активна"),
                ),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="person_who_has_subscribers",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
                (
                    "subscriber",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subscribers",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Подписчик",
                    ),
                ),
            ],
            options={
                "verbose_name": "Подписка",
                "verbose_name_plural": "Подписки",
                "unique_together": {("person", "subscriber")},
            },
        ),
    ]
