from django.shortcuts import redirect, render

from video.models import Video
from django.shortcuts import redirect
# Create your views here.
def online(request,uuid):
    video = Video.objects.get(uuid=uuid)
    return render(request, 'online.html', {'video':video.video.url})


def delete(request,uuid):
    if request.method=="POST":
        video = Video.objects.get(uuid=uuid)
        page=request.POST.get('page', 1)
        page=int(page)
        video.delete()
        return redirect(f"/?page={page}")
    else:
        page=request.GET.get('next', 1)
        page=int(page)
        return render(request,'delete_confirm.html', context={'uuid':uuid,'page':page})
