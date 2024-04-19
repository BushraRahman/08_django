from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from concerts.models import Song
from concerts.models import Artist
from django.views import View
from .forms import ArtistForm
from django.views.generic.edit import CreateView
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def index(request):
    return render(request, "concerts/concerts_index.html")

@login_required
def songsIndex(request):
    if request.method == 'POST':
        loadSongs()
    return render(request, "concerts/songs.html")

@login_required
def loadSongs():
    if not Song.objects.filter(title="Run").exists():
        Song.objects.create(title="Run", duration="00:10:30",genre="pop").save()
        Song.objects.create(title="My House", duration="00:08:30",genre="RNB").save()
        Song.objects.create(title="Pop", duration="00:02:26",genre="RNB").save()
# Create your views here.

class ArtistCreatebisView(LoginRequiredMixin,View):
    def post(self, request, *args, **kwargs):
       artist = get_object_or_404(Artist, pk=self.kwargs["pk"])
       # Create a form instance with POST data
       form = ArtistForm(request.POST, instance=movie)
       if form.is_valid():
           form.save()
           return JsonResponse({"success": True})
       else:
           return JsonResponse({"success": False, "errors": form.errors})
    def get(self, request, *args, **kwargs):
        artist = get_object_or_404(Artist, pk=self.kwargs["pk"])
        # Create a form instance with POST data
        form = ArtistForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "errors": form.errors})