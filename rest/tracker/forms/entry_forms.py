from django import forms

from tracker.models import Entry, Tag


class EntryForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Entry
        fields = ['title', 'description', 'type', 'status', 'priority', ]

    # def __init__(self, *args, **kwargs):
    #     super(EntryForm, self).__init__(*args, **kwargs)
    #     if self.instance:
    #         self.fields['tags'].initial = self.instance.tags.all()
