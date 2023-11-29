# Generated by Django 4.2 on 2023-06-12 08:36

import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import video.models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0004_alter_video_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='published_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to=video.models.get_movie_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv', 'mp3', 'ts'])], verbose_name='فایل ویدیو'),
        ),
    ]