# Generated by Django 3.2.13 on 2022-05-23 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('description', '0005_auto_20220522_1445'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='likedislike',
            options={'verbose_name': 'Оценка', 'verbose_name_plural': 'Оценки'},
        ),
    ]
