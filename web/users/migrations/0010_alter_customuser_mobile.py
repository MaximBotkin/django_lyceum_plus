# Generated by Django 3.2.13 on 2022-05-15 09:17

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='mobile',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[users.validators.validate_for_mobile], verbose_name='Номер телефона'),
        ),
    ]