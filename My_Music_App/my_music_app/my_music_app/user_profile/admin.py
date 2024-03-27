from django.contrib import admin

from my_music_app.user_profile.models import Profile


@admin.register(Profile)
class UserProfileAdmin(admin.ModelAdmin):
    pass
