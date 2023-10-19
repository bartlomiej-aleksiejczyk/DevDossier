from django import forms

from tracker.models import Entry


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('title', 'description', 'status', 'priority', 'app')
