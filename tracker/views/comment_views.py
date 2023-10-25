from django.shortcuts import get_object_or_404, redirect, render

from tracker.forms.comment_forms import CommentForm
from tracker.models import Entry, Attachment


def comment_create(request, app_pk, entry_pk):
    entry = get_object_or_404(Entry, pk=entry_pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            #comment.createdBy = request.user
            comment.entry = entry
            comment.save()

            if 'attachment' in request.FILES:
                attachment = Attachment(filePath=request.FILES['attachment'],
                                        #createdBy=request.user
                                        )
                attachment.save()
                comment.attachment = attachment
                comment.save()

            return redirect('entry_detail', app_pk=app_pk, pk=entry_pk)
    else:
        form = CommentForm()
    return render(request, 'comment/comment_form.html', {'form': form, 'entry': entry})
