from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from expenses_tracker.my_validators import validate_only_letters, MaxImageSizeValidator


class UserProfile(models.Model):
    MIN_NAME_LENGTH = 2
    MAX_NAME_LENGTH = 15
    BUDGET_DEFAULT = 0
    BUDGET_MIN = 0
    MAX_PHOTO_SIZE = 5.0
    IMAGE_FOLDER = 'profile_images/'
    first_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=[
            MinLengthValidator(MIN_NAME_LENGTH),
            validate_only_letters
        ]
    )
    last_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=[
            MinLengthValidator(MIN_NAME_LENGTH),
            validate_only_letters
        ],
        blank=False,
        null=False,

    )
    budget = models.FloatField(
        default=BUDGET_DEFAULT,
        validators=[
            MinValueValidator(BUDGET_MIN)
        ],
        blank=False,
        null=False,
    )
    profile_image = models.ImageField(
        upload_to=IMAGE_FOLDER,
        validators=(
            MaxImageSizeValidator(MAX_PHOTO_SIZE),
        ),
        blank=True,
        null=True,
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
