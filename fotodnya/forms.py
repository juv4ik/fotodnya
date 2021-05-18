from django import forms


class formPropose(forms.Form):
    Заголовок = forms.CharField(max_length=220)
    Информация = forms.CharField(widget=forms.Textarea)







