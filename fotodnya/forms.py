from django import forms
from .models import comments_fn

class formPropose(forms.Form):
    Заголовок = forms.CharField(max_length=220)
    Информация = forms.CharField(widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = comments_fn
        fields = ('comment', 'name', 'fotoNews')  #('name', 'email', 'comment')

