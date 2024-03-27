from django import forms

from my_music_app.user_profile.models import Profile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    widgets = {
        'username': forms.TextInput(attrs={'placeholder': 'First Name'}),
        'email': forms.TextInput(attrs={'placeholder': 'Email'}),
        'age': forms.TextInput(attrs={'placeholder': 'Age'}),
    }