from django.core.validators import MaxLengthValidator
from django.db import models

from my_music_app.my_validators import verify_only_letters_numbers_and_underscore


class Profile(models.Model):
    MAX_USERNAME_LENGTH = 15

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        null=False,
        blank=False,
        validators=(
            MaxLengthValidator(MAX_USERNAME_LENGTH),
            verify_only_letters_numbers_and_underscore,
        )
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username
