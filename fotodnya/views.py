from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin

from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm



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


class BlogDetailView(DetailView):
    model = fotoNews
    #context_object_name = 'fotoNews'
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['comments'] = comments_fn.objects.all()
        context['CommentForm'] = CommentForm()
        # And so on for more models
        return context


def aboutPage(request):
    return render(request, 'about.html')

