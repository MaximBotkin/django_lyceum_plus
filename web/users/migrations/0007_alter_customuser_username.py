# Generated by Django 3.2.12 on 2022-05-11 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=50, unique=True, verbose_name='Никнэйм'),
        ),
    ]
