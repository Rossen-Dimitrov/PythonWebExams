from django.shortcuts import render, redirect

from my_music_app.album.models import Album
from my_music_app.user_profile.forms import UserProfileForm
from my_music_app.utilities import get_user_profile


def add_profile(request):
    if get_user_profile() is not None:
        redirect('home page')
    form = UserProfileForm(request.GET)
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'profile': get_user_profile,
    }

    return render(request, 'core/home-no-profile.html', context=context)


def details_profile(request):

    context = {
        'profile': get_user_profile,
        'albums_count': Album.objects.all().count()
    }

    return render(request, 'profile/profile-details.html', context=context)


def delete_profile(request):
    profile = get_user_profile()

    if request.method == 'POST':
        profile.delete()
        Album.objects.all().delete()
        return redirect('home page')

    return render(request, 'profile/profile-delete.html')
