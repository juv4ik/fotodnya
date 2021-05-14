from django import forms
from .models import Comment

class formPropose(forms.Form):
    Заголовок = forms.CharField(max_length=220)
    Информация = forms.CharField(widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')