from django.shortcuts import render, redirect

from my_music_app.album.models import Album
from my_music_app.utilities import get_user_profile


def home_page(request):
    profile = get_user_profile()
    all_albums = Album.objects.all()
    if not profile:
        return redirect('add profile')

    context = {
        'profile': profile,
        'all_albums': all_albums,
    }
    return render(request, 'core/home-with-profile.html', context=context)
