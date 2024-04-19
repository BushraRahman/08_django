from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from concerts.models import Song, Artist, Concert
from django.views import View
from .forms import ArtistForm
from django.views.generic.edit import CreateView
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

@login_required
def index(request):
    return render(request, "concerts/index.html")

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

@login_required
def concertsIndex(request):
    if not Concert.objects.filter(name="Ode To You").exists():
        Concert.objects.create(name="The Fifth World Tour", date="2023-4-18",venue="Great Strahov Stadium").save()
        Concert.objects.create(name="Follow", date="2023-4-18",venue="Ohio Stadium").save()
        Concert.objects.create(name="Ode To You", date="2023-4-18",venue="Beijing National Stadium").save()
    return render(request, "concerts/concerts.html")

class ArtistCreateView(LoginRequiredMixin, CreateView):
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
        return reverse_lazy("concerts:artists")