from django.shortcuts import render, redirect

from my_music_app.album.forms import AlbumCreateForm, AlbumDeleteForm
from my_music_app.album.models import Album
from my_music_app.utilities import get_user_profile


def details_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    context = {
        'profile': get_user_profile,
        'album': album
    }
    return render(request, 'album/album-details.html', context=context)


def add_album(request):
    form = AlbumCreateForm(request.GET)
    if request.method == 'POST':
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'profile': get_user_profile,
        'form': form,
    }
    return render(request, 'album/add-album.html', context=context)


def edit_album(request, pk):
    album = Album.objects.filter(pk=pk).get()
    form = AlbumCreateForm(instance=album)
    if request.method == 'POST':
        form = AlbumCreateForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album details page', pk=pk)

    context = {
        'form': form,
        "pk": pk
    }

    return render(request, 'album/edit-album.html', context=context)


def delete_album(request, pk):
    album = Album.objects.filter(pk=pk).get()
    form = AlbumDeleteForm(instance=album)
    if request.method == 'POST':
        album.delete()
        return redirect('home page')

    context = {
        'form': form,
        'pk': pk,
    }

    return render(request, 'album/delete-album.html', context=context)
