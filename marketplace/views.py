from django.shortcuts import render
from .models import Artwork

def home(request):
    artworks = Artwork.objects.all()
    return render(request, 'marketplace/home.html', {'artworks': artworks})
