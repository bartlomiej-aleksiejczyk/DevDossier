from django.shortcuts import get_object_or_404, render, redirect
from tracker.forms.app_forms import AppForm
from tracker.models import App


def app_list(request):
    apps = App.objects.all()
    return render(request, 'app/app_list.html', {'apps': apps})


def app_create(request):
    if request.method == "POST":
        form = AppForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_list')
    else:
        form = AppForm()
    return render(request, 'app/app_form.html', {'form': form})


def app_detail(request, pk):
    app = get_object_or_404(App, pk=pk)
    entries = app.entries.all()
    return render(request, 'app/app_detail.html', {'app': app, 'entries': entries})


def app_edit(request, pk):
    app = get_object_or_404(App, pk=pk)
    if request.method == "POST":
        form = AppForm(request.POST, instance=app)
        if form.is_valid():
            form.save()
            return redirect('app_detail', pk=app.pk)
    else:
        form = AppForm(instance=app)
    return render(request, 'app/app_form.html', {'form': form})


def app_delete(request, pk):
    if request.method == "POST":
        app = get_object_or_404(App, pk=pk)
        app.delete()
        return redirect('app_list')
