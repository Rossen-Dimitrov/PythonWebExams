from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from exam.app_profile.models import AppProfile
from exam.recipe.forms import RecipeCreatForm
from exam.recipe.models import Recipe


class CatalogListView(ListView):
    template_name = 'recepie/catalogue.html'
    model = Recipe
    extra_context = {
        'profile': AppProfile.objects.first()
    }


class RecipeCreatView(CreateView):
    template_name = 'recepie/create-recipe.html'
    model = Recipe
    form_class = RecipeCreatForm
    success_url = reverse_lazy('catalogue')
    extra_context = {
        'profile': AppProfile.objects.first()
    }


class RecipeDetailsView(DetailView):
    template_name = 'recepie/details-recipe.html'
    model = Recipe
    extra_context = {
        'profile': AppProfile.objects.first()
    }


class RecipeEditView(UpdateView):
    template_name = 'recepie/edit-recipe.html'
    model = Recipe
    form_class = RecipeCreatForm
    success_url = reverse_lazy('catalogue')
    extra_context = {
        'profile': AppProfile.objects.first()
    }


class RecipeDeleteView(DeleteView):
    template_name = 'recepie/delete-recipe.html'
    model = Recipe
    success_url = reverse_lazy('catalogue')
    extra_context = {
        'profile': AppProfile.objects.first()
    }

