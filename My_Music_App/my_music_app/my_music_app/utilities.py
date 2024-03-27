from my_music_app.user_profile.models import Profile


def get_user_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:

        return None
