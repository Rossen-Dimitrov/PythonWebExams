from django import forms

from expenses_tracker.user_profile.models import UserProfile


class UserProfileBaseForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['budget', 'first_name', 'last_name', 'profile_image']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_image': 'Profile Image',
        }


class UserProfileAddForm(UserProfileBaseForm):
    pass


class UserProfileEditForm(UserProfileBaseForm):
    pass


class UserProfileDeleteForm(UserProfileBaseForm):
    pass
