from django.shortcuts import render
from django.http import HttpResponse
from concerts.models import Song
from concerts.models import Artist
from django.views import View
from django.views.generic.edit import CreateView

def index(request):
    return render(request, "concerts/concerts_index.html")

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

class ArtistCreateView(CreateView):
    model = Artist
    fields = ['name','concerts','songs']
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
        self.request, messages.SUCCESS,
        'Artist "{artist_name}" has been created'.format(
        artist_name=self.object.name))
        return response
    def get_success_url(self):
        return reverse_lazy("concerts:artists", args=[self.object.id])