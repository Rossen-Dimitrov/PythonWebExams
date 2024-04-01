from django.shortcuts import render, redirect
from fruitipedia_app.fruit.models import Fruit
from fruitipedia_app.user_profile.forms import CreateUserProfileForm, EditUserProfileForm
from fruitipedia_app.utils import get_user_profile


def profile_details(request):
    profile = get_user_profile()
    count = Fruit.objects.all().count()

    context = {
        'profile': profile,
        'posts_count': count
    }

    return render(request, 'profile/details-profile.html', context=context)


def create_profile(request):
    form = CreateUserProfileForm
    if request.method == 'POST':
        form = CreateUserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index page')

    context = {
        'form': form,
    }

    return render(request, template_name='profile/create-profile.html', context=context)


def edit_profile(request):
    profile = get_user_profile()
    form = EditUserProfileForm(instance=profile)
    if request.method == 'POST':
        form = EditUserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details page')

    context = {
        'form': form
    }

    return render(request, 'profile/edit-profile.html', context=context)


def delete_profile(request):
    profile = get_user_profile()
    if request.method == 'POST':
        profile.delete()
        Fruit.objects.all().delete()
        return redirect('index page')

    return render(request, 'profile/delete-profile.html')