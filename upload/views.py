from datetime import datetime
import json
import math
import os
import cv2
from django.http import HttpResponse
from django.shortcuts import render

from video.forms import CreateVideo
from video.models import Actor, Video

# Create your views here.


def get_gif_path(self, filename):
    ext = filename.split('.')
    ext = ext[-1]
    fileStat = os.stat(self.video.path)
    rendered_time = datetime.fromtimestamp(fileStat.st_mtime)
    title = f'{rendered_time.year}-{rendered_time.month}-{rendered_time.day}{rendered_time.hour}{rendered_time.minute}'
    title = title.lower().replace(' ', '_')
    title = title+'_gif'
    return f'videos/{self.uuid}/{title}.gif'

def index(request):
    if request.method == "GET":
        return render(request, 'upload.html', {'actors': Actor.objects.all()})
    else:
        form = CreateVideo(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            video =request.FILES.get('video')
            instance = Video(title=cleaned_data['title'],video=video)
            instance.save()
            gif_name = get_gif(instance)
            instance.cast.set(cleaned_data['cast'])
            date = set_date(instance)
            instance.gif.name = gif_name
            instance.date = date
            instance.save()
            return render(request, 'upload.html', {'actors': Actor.objects.all()})
        else:
            return render(request, 'upload.html', {'actors': Actor.objects.all(), 'errors': form.errors})
        
def get_gif(video):
    v = cv2.VideoCapture(video.video.path)
    frames = v.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = v.get(cv2.CAP_PROP_FPS)
    seconds = round(frames / fps)
    duration = math.ceil(seconds / 60)
    pass_sec = duration/2 * 60
    gif_name = get_gif_path(video, video.video.name.split('/')[-1])
    gif_name2 = os.path.join(os.getcwd(), f'media/{gif_name}')
    gif_name2 = gif_name2.replace('\\', "/")
    command = f'ffmpeg -ss {pass_sec} -t 10 -i "{video.video.path}" -vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 "{gif_name2}"'
    print(command)
    os.system(command)
    return gif_name

def set_date(video):
    fileStat = os.stat(video.video.path)
    rendered_time = datetime.fromtimestamp(fileStat.st_mtime)
    return f'{rendered_time.year}-{rendered_time.month}-{rendered_time.day}{rendered_time.hour}-{rendered_time.minute}'
