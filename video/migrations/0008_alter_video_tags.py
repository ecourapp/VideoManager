# Generated by Django 4.2.7 on 2023-11-29 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0007_alter_video_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='tags',
            field=models.ManyToManyField(blank=True, to='video.tag'),
        ),
    ]
