from django.shortcuts import get_object_or_404, redirect, render

from tracker.forms.entry_forms import EntryForm
from tracker.models import Entry


def entry_list(request):
    entries = Entry.objects.all()
    return render(request, 'entry/entry_list.html', {'entries': entries})


def entry_detail(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    return render(request, 'entry/entry_detail.html', {'entry': entry})


def entry_create(request):
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entry_list')
    else:
        form = EntryForm()
    return render(request, 'entry/entry_form.html', {'form': form})


def entry_edit(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == "POST":
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('entry_detail', pk=entry.pk)
    else:
        form = EntryForm(instance=entry)
    return render(request, 'entry/entry_form.html', {'form': form})


def entry_delete(request, pk):
    if request.method == "POST":
        entry = get_object_or_404(Entry, pk=pk)
        entry.delete()
        return redirect('entry_list')
