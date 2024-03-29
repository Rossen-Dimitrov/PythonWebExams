from expenses_tracker.user_profile.models import UserProfile


def get_user_profile():
    try:
        return UserProfile.objects.get()
    except UserProfile.DoesNotExist:
        return None
