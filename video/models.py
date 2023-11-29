from datetime import datetime
import os
import time
from django.db import models
from django.dispatch import receiver
from django.utils.crypto import get_random_string
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext as _

# Create your models here.

def get_movie_path(self, filename):
    ext = filename.split('.')
    ext = ext[-1]
    # fileStat = os.stat(self.video.path)
    # rendered_time = datetime.fromtimestamp(fileStat.st_mtime)
    title = filename
    title = title.lower().replace(' ', '_')
    return f'videos/{self.uuid}/{title}'

def get_gif_path(self, filename):
    ext = filename.split('.')
    ext = ext[-1]
    fileStat = os.stat(self.video.path)
    rendered_time = datetime.fromtimestamp(fileStat.st_mtime)
    title = f'{rendered_time.year}-{rendered_time.month}-{rendered_time.day}{rendered_time.hour}{rendered_time.minute}'
    title = title.lower().replace(' ', '_')
    title = title+'_gif'
    return f'videos/{self.uuid}/{title}.gif'

def generate_id_length():
    return get_random_string(10)

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
class Actor(models.Model):
    CHOICES_SEX = (('male','male'),('female', 'female'))
    name = models.CharField(max_length=300)
    sex = models.CharField(max_length=300, choices=CHOICES_SEX)
    def __str__(self) -> str:
        return self.name

class Video(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True)
    uuid = models.CharField(default=generate_id_length,max_length=10,unique=True)
    video = models.FileField(
        verbose_name=_("فایل ویدیو"),
        upload_to=get_movie_path,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv', 'mp3','ts'])
        ])
    date = models.CharField(max_length=300, null=True,blank=True)
    cast = models.ManyToManyField(Actor, blank=True)
    gif = models.FileField(
        verbose_name=_("فایل گیف"),
        upload_to=get_gif_path,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['gif', 'png'])
        ],null=True, blank=True)
    
    published_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    def __str__(self) -> str:
        if self.title:
            return self.title
        elif self.date:
            return self.date
        else:
            return self.video.name.split('/')[-1]    
    class Meta:
        ordering = ['-published_at']


        



@receiver(models.signals.post_delete, sender=Video)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    main_folder = "media/"+get_movie_path(instance,"")
    if instance.video:
        video_path = instance.video.path
        if os.path.isfile(video_path):
            os.remove(video_path)
    if instance.gif:
        gif_path = instance.gif.path
        if os.path.isfile(gif_path):
            os.remove(gif_path)
    try:
        os.rmdir(main_folder)
    except Exception as e:
        pass 
    
