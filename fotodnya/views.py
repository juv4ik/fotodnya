from django.shortcuts import render
from django.views.generic import DetailView
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def indexPage(request):
    object_list = list(reversed(fotoNews.objects.all()))
    paginator = Paginator(object_list, 8)  # 8 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'index.html',
                  {'page': page,
                   'posts': posts})

# def indexPage(request):
#    posts = reversed(fotoNews.objects.all())
#    return render(request, 'index.html', {'posts': posts})

class BlogDetailView(DetailView):
    model = fotoNews
    template_name = 'post_detail.html'

def aboutPage(request):
    return render(request, 'about.html')






