from django import forms
from tracker.models import Comment


class CommentForm(forms.ModelForm):
    attachment = forms.FileField(required=False)

    class Meta:
        model = Comment
        fields = ['body', 'attachment']
