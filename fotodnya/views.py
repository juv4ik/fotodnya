from django.shortcuts import render
from .models import *


def indexPage(request):
    posts = reversed(fotoNews.objects.all())
    return render(request, 'index.html', {'posts': posts})



