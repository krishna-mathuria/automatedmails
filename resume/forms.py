from django import forms
from .models import Files


class FileForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ('Excel', 'Html', 'Subject')
