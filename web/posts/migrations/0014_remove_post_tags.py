# Generated by Django 3.2.13 on 2022-05-23 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0013_auto_20220519_1023"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="tags",
        ),
    ]
