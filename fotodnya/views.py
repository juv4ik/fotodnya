from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


def indexPage(request):
    posts = reversed(fotoNews.objects.all())
    return render(request, 'index.html', {'posts': posts})

class BlogDetailView(DetailView):
    model = fotoNews
    template_name = 'post_detail.html'




