from django import forms
from tracker.models import App


class AppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ('name', 'description')
