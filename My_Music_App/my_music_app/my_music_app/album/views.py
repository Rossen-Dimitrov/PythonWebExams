from django.shortcuts import render

from my_music_app.utilities import get_user_profile


def details_album(request):
    context = {
        'profile': get_user_profile,
    }
    return render(request, 'album/album-details.html', context=context)


def add_album(request):
    context = {
        'profile': get_user_profile,
    }
    return render(request, 'album/add-album.html', context=context)


def edit_album(request):
    return render(request, 'album/edit-album.html')


def delete_album(request):
    return render(request, 'album/delete-album.html')
