from django.shortcuts import render, redirect

from my_music_app.album.models import Album
from my_music_app.user_profile.views import add_profile
from my_music_app.utilities import get_user_profile


def home_page(request):
    if not get_user_profile():
        return add_profile(request)

    all_albums = Album.objects.all()

    context = {
        'profile': True,
        'all_albums': all_albums,
    }
    return render(request, 'core/home-with-profile.html', context=context)
