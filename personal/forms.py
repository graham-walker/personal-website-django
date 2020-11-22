from django import forms
from personal.models import File
from taggit.forms import TagWidget

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'file']
