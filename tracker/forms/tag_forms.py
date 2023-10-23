from django import forms
from tracker.models import Tag


class TagForm(forms.ModelForm):
    tagColor = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}), label="Tag Color")

    class Meta:
        model = Tag
        fields = ['tagString', 'tagColor']
        labels = {
            'tagString': 'Tag Name',
            'tagColor': 'Tag Color'
        }
