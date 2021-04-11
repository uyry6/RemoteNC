from django import forms

from .models import IMG

class ImgForm(forms.ModelForm):
    class Meta:
        model  = IMG
        fields = ['img']
