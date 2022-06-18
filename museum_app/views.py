from django.shortcuts import render
from .models import *
from .admin import *

# Create your views here.

def rooms():
    roomslist = Room.objects.all()
    return roomslist

def exhibition_artworks():
    artworkslist = Artwork.objects.all()
    exibition_artworks = []
    for artwork in artworkslist:
        if str(current_state(artwork)) == 'Exhibition':
            exibition_artworks.append(artwork)
    return exibition_artworks


def home(request):
    return render(request, 'pages/home.html', {'rooms': rooms()})

def contact(request):
    return render(request, 'pages/contact.html', {'rooms': rooms()})

def about(request):
    return render(request, 'pages/about.html', {'rooms': rooms()})

def catalog(request):
    artworkslist = exhibition_artworks()
    return render(request, 'pages/catalog.html', {'rooms':rooms(), 'artworkslist':artworkslist})

def rooms_catalog(request, room):
    room_artworks = []
    for artwork in exhibition_artworks():
        if str(artwork.room) == str(room):
            room_artworks.append(artwork)
    return render(request, 'pages/catalog.html', {'rooms':rooms(), 'artworkslist':room_artworks})
