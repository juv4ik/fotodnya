import time
from datetime import datetime

from django.contrib.postgres.fields import ArrayField
from django.db import models

class fotoNews(models.Model):
    title = models.CharField(max_length=120)
    img = models.ImageField(upload_to='static/images/', null=True, blank=True, default='static/images/default.jpg')
    author = models.CharField(max_length=120, blank=True)
    url_from = models.URLField(max_length=300, default='http://fotodnya.site', blank=True)
    timepostdate = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'


