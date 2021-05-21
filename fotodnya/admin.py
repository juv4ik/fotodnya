from django.contrib import admin
from .models import fotoNews, comments_fn
admin.site.register(fotoNews)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('created', 'name', 'comment', 'email', 'fotoNews', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'comment')
admin.site.register(comments_fn, CommentAdmin)

