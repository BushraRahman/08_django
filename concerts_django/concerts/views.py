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
import datetime

@login_required
def index(request):
    context = {"songs_link": reverse_lazy("concerts:songs"), "concerts_link": reverse_lazy("concerts:concerts"), "artists_link": reverse_lazy("concerts:artists")}
    print(context)
    return render(request, "concerts/index.html")

@login_required
def songsIndex(request):
    if not Song.objects.filter(title="Hypertonic").exists():
        Song.objects.create(title="Hypertonic", duration="00:8:16",genre="pop").save()
        Song.objects.create(title="Heartbeat", duration="00:08:30",genre="RNB").save()
        Song.objects.create(title="DU DU DU", duration="00:02:26",genre="RNB").save()
    return render(request, "concerts/songs.html")
    
# Create your views here.

@login_required
def concertsIndex(request):
    if not Concert.objects.filter(name="Ode To Who?").exists():
        Concert.objects.create(name="The Fourth World Tour", date="2023-4-18",venue="Great Strahov Stadium").save()
        Concert.objects.create(name="Lead", date="2021-3-7",venue="Ohio Stadium").save()
        Concert.objects.create(name="Ode To Who?", date="2014-11-29",venue="Beijing National Stadium").save()
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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        concerts_list = []
        for concert in Concert.objects.all():
            concerts_list.append({"id": concert.id, "name": concert.name, "date": str(concert.date), "venue": concert.venue})
        context["concerts"] = concerts_list
        songs_list = []
        for song in Song.objects.all():
            songs_list.append({"id": song.id, "title": song.title, "duration": str(song.duration), "genre": song.genre})
        context["songs"] = songs_list
        print("context", context)
        return context
    def get_success_url(self):
        return reverse_lazy("concerts:artists")