from django.db import models
from django.urls import path

class fotoNews(models.Model):
    title = models.CharField(max_length=120)
    img = models.ImageField(upload_to='static/images/', null=True, blank=True, default='static/images/default.jpg')
    author = models.CharField(max_length=120, blank=True)
    url_from = models.URLField(max_length=300, default='http://fotodnya.site', blank=True)
    timepostdate = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'


class comments_fn(models.Model):
    fotoNews = models.ForeignKey(fotoNews, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=80)
    email = models.EmailField(default='none')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.fotoNews, self.comment)

