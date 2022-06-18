from django.shortcuts import render
from .models import *

# Create your views here.

def exibition_artworks():
    artworkslist = Artwork.objects.all()
    exibition_artworks = []
    for artwork in artworkslist:
        if str(current_state(artwork)) == 'Exibition':
            exibition_artworks.append(artwork)
    return exibition_artworks
def home(request):
    return render(request, 'pages/home.html')

def contact(request):
    return render(request, 'pages/contact.html')

def about(request):
    return render(request, 'pages/about.html')

def catalog(request):
    return render(request, 'pages/catalog.html', {'rooms':rooms(), 'artworkslist':artworkslist})

