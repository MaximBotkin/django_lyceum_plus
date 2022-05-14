# Generated by Django 3.2.13 on 2022-05-12 18:30

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_merge_20220511_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=50, unique=True, validators=[users.validators.validate_for_username], verbose_name='Никнэйм'),
        ),
    ]