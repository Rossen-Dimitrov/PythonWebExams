from django.shortcuts import render, redirect

from fruitipedia_app.core.views import dashboard
from fruitipedia_app.fruit.forms import FruitCreateForm, FruitEditForm, FruitDeleteForm
from fruitipedia_app.fruit.models import Fruit


def details_fruit(request, fruitId):
    fruit = Fruit.objects.get(pk=fruitId)

    context = {
        'fruit': fruit,
        'profile': True
    }
    return render(request, 'fruit/details-fruit.html', context=context)


def create_fruit(request):
    form = FruitCreateForm
    if request.method == 'POST':
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return dashboard(request)

    context = {
        'form': form,
        'profile': True
    }
    return render(request, 'fruit/create-fruit.html', context=context)


def edit_fruit(request, fruitId):
    fruit = Fruit.objects.get(id=fruitId)
    form = FruitEditForm(instance=fruit)
    if request.method == 'POST':
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return dashboard(request)

    context = {
        'form': form,
        'fruitId': fruitId
    }
    return render(request, 'fruit/edit-fruit.html', context=context)


def delete_fruit(request, fruitId):
    fruit = Fruit.objects.get(id=fruitId)
    form = FruitDeleteForm(instance=fruit)
    if request.method == 'POST':
        fruit.delete()
        return dashboard(request)

    context = {
        'form': form,
        'fruitId': fruitId
    }
    return render(request, 'fruit/delete-fruit.html', context=context)
