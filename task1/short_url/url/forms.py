from django import forms
from . import models

class ShortenUrlCreateForm(forms.ModelForm):
    class Meta:
        model = models.ShortenedUrl
        fields = ['origin']
