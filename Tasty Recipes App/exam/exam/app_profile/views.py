from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from exam import app_profile
from exam.app_profile.forms import ProfileCreateForm
from exam.app_profile.models import AppProfile
from exam.recipe.models import Recipe


class ProfileCreatView(CreateView):
    template_name = 'profile/create-profile.html'
    model = AppProfile
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')


class ProfileDetailsView(DetailView):
    template_name = 'profile/details-profile.html'
    model = AppProfile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = AppProfile.objects.first()
        context['count'] = Recipe.objects.count()
        return context


class ProfileEditView(UpdateView):
    template_name = 'profile/edit-profile.html'
    model = AppProfile
    form_class = ProfileCreateForm
    extra_context = {
        'profile': AppProfile.objects.first()
    }

    def get_success_url(self):
        return reverse("profile details page", kwargs={'pk': self.object.pk})


class ProfileDeleteView(DeleteView):
    template_name = 'profile/delete-profile.html'
    model = AppProfile

    extra_context = {
        'profile': AppProfile.objects.first()
    }
    Recipe.objects.all().delete()
    success_url = reverse_lazy('home')
