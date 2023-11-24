from django.shortcuts import render, redirect
from tracker.forms.tag_forms import TagForm
from tracker.models import Tag


def tag_create(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tag_list')
    else:
        form = TagForm()
    return render(request, 'tag/tag_form.html', {'form': form})


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'tag/tag_list.html', {'tags': tags})
