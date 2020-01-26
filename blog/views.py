from django.shortcuts import render
from django.conf import settings
from .models import Post
import os

def landing(request):
    slides = []
    static_dir = os.path.join(os.path.join(os.path.join(os.path.join(settings.BASE_DIR, 'blog'), 'static'), 'blog'), 'slides')
    for file in os.listdir(static_dir):
        if file.endswith('.jpg'):
            slides.append(file)
    return render(request, 'blog/landing.html', {'slides': slides})
# Create your views here.
