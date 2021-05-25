from django import forms
from django.forms import Textarea, TextInput
from django.http import request

from .models import comments_fn
from django.db import models

class formPropose(forms.Form):
    Заголовок = forms.CharField(max_length=220)
    Информация = forms.CharField(widget=forms.Textarea)



class CommentForm(forms.ModelForm):
    class Meta:
        model = comments_fn
        fields = ('comment', 'name', 'fotoNews')
        widgets = {
            "name": Textarea(attrs={
                'class': 'username_get',
                'value': '{{ request.user.username.title }}'
            })
        }



