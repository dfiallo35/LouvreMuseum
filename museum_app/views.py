from django.shortcuts import render
from .models import Artwork

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def catalog(request):
    artworkslist = Artwork.objects.all()
    return render(request, 'pages/catalog.html', {'artworkslist':artworkslist})