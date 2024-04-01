from django import forms

from fruitipedia_app.user_profile.models import UserProfile


class UserProfileBaseForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'password']
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }


class CreateUserProfileForm(UserProfileBaseForm):
    pass


class EditUserProfileForm(UserProfileBaseForm):
    class Meta:
        model = UserProfile
        exclude = ['password', 'email']


class DeleteUserProfileForm(UserProfileBaseForm):
    pass
