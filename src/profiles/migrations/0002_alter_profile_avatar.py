# Generated by Django 4.2.2 on 2023-06-26 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='shehab.png', upload_to='avatars'),
        ),
    ]
