

from django import forms
from video.models import Video

class CreateVideo(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title','video','cast']

