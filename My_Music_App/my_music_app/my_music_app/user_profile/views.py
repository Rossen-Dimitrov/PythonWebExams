from django.shortcuts import render, redirect

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
    return render(request, 'profile/profile-details.html')


def delete_profile(request):
    return render(request, 'profile/profile-delete.html')
