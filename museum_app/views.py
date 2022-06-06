from django.shortcuts import render
from .models import Artwork

# Create your views here.

def home_page(request):
    return render(request, 'pages/home.html')

# def catalog(request):
#     return render(request, 'pages/catalog.html')

def catalog(request):
    artworkslist = Artwork.objects.all()
    return render(request, 'pages/catalog.html', {'artworkslist':artworkslist})