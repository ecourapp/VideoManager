import math
from django.http import HttpResponse
import json
from django.shortcuts import render
from video.models import Video,Tag
from video.serializer import serializer
import json
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.

def videos_list(request):
    errors = []
    page = request.GET.get('page', 1)
    page = int(page)
    first = (page-1)*21
    last = page*21
    videos = Video.objects.all()[first:last]
    serialized = [serializer(video) for video in videos]

    return HttpResponse(json.dumps(serialized), content_type="application/json")
    
def get_tags(searched_val):
    results =[]
    for tag in Tag.objects.all():
        splitted = ''.join(tag.name.lower().split(' '))
        if splitted.find(searched_val) != -1:
            videos = Video.objects.filter(tags__name__in=[tag.name])
            results.extend([serializer(video) for video in videos])
    return results

def index(request):
    page = request.GET.get('page',1)
    page=int(page)
    last_page = math.ceil(len(Video.objects.all()) / 21)
    first_page = 1
    context = {
        'has_next': page < last_page,
        'hast_prev': page > 1,
        'next': page + 1 if page < last_page else None,
        'prev': page -1 if page > 1 else None,
        'page_obj': range(1,last_page+1), 
        'page': page
    }
    return render(request,'home.html',context=context)

def search(request, search_val):
    if search_val is not None:
        results = []
        for video in Video.objects.all():
            splitted = ''.join(video.title.lower().split(' '))
            if splitted.find(search_val) != -1:
                serialized = serializer(video)
                results.append(serialized)
        tags = get_tags(search_val)
        results.extend(tags)
        return HttpResponse(json.dumps(results), content_type="application/json")

def fix(request):
    names_list = []
    for video in Video.objects.all():
        names_list.append(video.title)
    with open("names.txt", "w", encoding="utf-8") as f:
        f.write(json.dumps(names_list))
    return HttpResponse()
