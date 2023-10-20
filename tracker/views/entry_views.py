from django.shortcuts import get_object_or_404, redirect, render

from tracker.forms.entry_forms import EntryForm
from tracker.models import Entry, App


def entry_list(request, app_pk):
    app = get_object_or_404(App, pk=app_pk)
    entries = app.entries.all()
    return render(request, 'entry/entry_list.html', {'entries': entries, "app_pk": app_pk})


def entry_detail(request, app_pk, pk):
    entry = get_object_or_404(Entry, pk=pk)
    return render(request, 'entry/entry_detail.html', {'entry': entry, "app_pk": app_pk})


def entry_create(request, app_pk):
    app = get_object_or_404(App, pk=app_pk)

    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.app = app
            entry.save()
            app = get_object_or_404(App, pk=app_pk)
            return redirect('entry_list_for_app', app_pk=app.pk)
    else:
        form = EntryForm()
    return render(request, 'entry/entry_form.html', {'form': form, 'app': app})


def entry_edit(request, app_pk, pk):
    app = get_object_or_404(App, pk=app_pk)
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == "POST":
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('entry_detail', pk=entry.pk)
    else:
        form = EntryForm(instance=entry)
    return render(request, 'entry/entry_form.html', {'form': form, 'app': app})


def entry_delete(request, app_pk, pk):
    if request.method == "POST":
        entry = get_object_or_404(Entry, pk=pk)
        entry.delete()
        app = get_object_or_404(App, pk=app_pk)
        entries = app.entries.all()
        return render(request, 'app/app_detail.html', {'app': app, 'entries': entries})
