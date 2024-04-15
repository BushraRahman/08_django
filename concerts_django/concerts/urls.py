from django.urls import path

from . import views

app_name = "concerts"

urlpatterns = [
   path("", views.index, name="index"),
   path("songs",views.songsIndex, name="songs"),
   path("artists",views.ArtistCreateView.as_view(), name="artists")
]
