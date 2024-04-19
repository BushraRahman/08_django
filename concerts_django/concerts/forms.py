from django import forms

from .models import Artist

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'concerts', 'songs']
        widgets = {
            'running_time': forms.TimeInput(),
            'release_date': forms.DateInput()
        }