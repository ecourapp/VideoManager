from home import views
from django.urls import path


app_name="home"

urlpatterns = [
    path('list', views.videos_list, name="list"),
    path('search/<str:search_val>', views.search, name="search"),
    path("fix", views.fix),
    path('', views.index,name="home"),

]
