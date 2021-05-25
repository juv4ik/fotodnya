from django.contrib import admin
from .models import fotoNews, comments_fn

class fotoNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'timepostdate', 'active')
    list_filter = ('active', 'timepostdate')
    search_fields = ('title', 'author', 'description', 'url_from')
admin.site.register(fotoNews, fotoNewsAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('created', 'name', 'comment', 'email', 'fotoNews', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'comment')
admin.site.register(comments_fn, CommentAdmin)

