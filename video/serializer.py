from video.models import Video


def serializer(video:Video):
    new_form = {
        "title":video.title,
        "uuid":video.uuid,
        "video": video.video.url,
        "gif": video.gif.url 
        }
    return new_form