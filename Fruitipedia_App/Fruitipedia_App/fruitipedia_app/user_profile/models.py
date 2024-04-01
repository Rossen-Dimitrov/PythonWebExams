from django.db import models

from django.core.validators import MinLengthValidator
from django.db import models

from fruitipedia_app.my_validators import validate_starts_with_letter


class UserProfile(models.Model):
    FIRST_NAME_MAX_LENGTH = 25
    FIRST_NAME_MIM_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 35
    LAST_NAME_MIM_LENGTH = 1
    EMAIL_MAX_LENGTH = 40
    PASS_MAX_LENGTH = 20
    PASS_MIN_LENGTH = 8

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(FIRST_NAME_MIM_LENGTH),
            validate_starts_with_letter
        ],
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(LAST_NAME_MIM_LENGTH),
            validate_starts_with_letter
        ],
        null=False,
        blank=False
    )

    email = models.EmailField(
        max_length=EMAIL_MAX_LENGTH,
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=PASS_MAX_LENGTH,
        validators=[
            MinLengthValidator(PASS_MIN_LENGTH)
        ]
    )

    image_url = models.URLField(
        null=True,
        blank=True
    )

    age = models.IntegerField(
        default=18,
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

