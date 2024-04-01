from django.shortcuts import render, redirect

from fruitipedia_app.fruit.models import Fruit
from fruitipedia_app.user_profile.views import create_profile
from fruitipedia_app.utils import get_user_profile


def index(request):
    profile = get_user_profile()
    if not profile:
        return redirect('profile create page')
    context = {
        'profile': profile
    }
    return render(request, 'core/index.html', context=context)


def dashboard(request):
    profile = get_user_profile()
    fruits = Fruit.objects.all()
    context = {
        'all_fruits': fruits,
        'profile': profile
    }

    return render(request, 'core/dashboard.html', context=context)

