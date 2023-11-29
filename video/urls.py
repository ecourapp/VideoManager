
from django.urls import path
from video import views

app_name = 'video'

urlpatterns= [
    path('online/<str:uuid>', views.online, name="online"),
    path('delete/<str:uuid>', views.delete, name="delete"),
]