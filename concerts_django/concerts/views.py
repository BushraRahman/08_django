from django.shortcuts import render
from django.http import HttpResponse
from concerts.models import Song

def index(request):
    return render(request, "concerts/concerts_form.html")

def songsIndex(request):
    if request.method == 'POST':
        loadSongs()
    return render(request, "concerts/songs.html")

def loadSongs():
    if not Song.objects.filter(title="Run").exists():
        Song.objects.create(title="Run", duration="00:10:30",genre="pop").save()
        Song.objects.create(title="My House", duration="00:08:30",genre="RNB").save()
        Song.objects.create(title="Pop", duration="00:02:26",genre="RNB").save()
# Create your views here.
