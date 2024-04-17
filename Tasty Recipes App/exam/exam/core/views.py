from django.shortcuts import render
from django.views.generic import TemplateView

from exam.app_profile.models import AppProfile


class HomePageView(TemplateView):
    template_name = 'core/home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = AppProfile.objects.first()
        return context



