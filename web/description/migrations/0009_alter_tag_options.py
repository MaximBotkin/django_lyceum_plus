# Generated by Django 3.2.13 on 2022-05-24 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("description", "0008_tag_taggedwhatever"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tag",
            options={"verbose_name": "Тэг", "verbose_name_plural": "Тэги"},
        ),
    ]