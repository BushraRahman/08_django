from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "concerts/concerts_form.html")

# Create your views here.
