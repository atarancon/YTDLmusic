from django import forms

class NameForm(forms.Form):
    url_link = forms.CharField(label='url_link', max_length=2048)
