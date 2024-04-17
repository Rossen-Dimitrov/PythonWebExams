from django import forms
from exam.app_profile.models import AppProfile


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = AppProfile
        fields = ['nickname', 'first_name', 'last_name', 'chef']
