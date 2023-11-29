from django.contrib import admin

from video.models import Actor, Video, Tag

# Register your models here.
admin.site.register(Video)
admin.site.register(Actor)
admin.site.register(Tag)