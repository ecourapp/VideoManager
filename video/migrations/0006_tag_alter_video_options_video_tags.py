# Generated by Django 4.2 on 2023-07-10 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0005_video_published_at_alter_video_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['-published_at']},
        ),
        migrations.AddField(
            model_name='video',
            name='tags',
            field=models.ManyToManyField(to='video.tag'),
        ),
    ]
