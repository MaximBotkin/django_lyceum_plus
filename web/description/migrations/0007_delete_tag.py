# Generated by Django 3.2.13 on 2022-05-23 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0014_remove_post_tags"),
        ("description", "0006_alter_likedislike_options"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Tag",
        ),
    ]
