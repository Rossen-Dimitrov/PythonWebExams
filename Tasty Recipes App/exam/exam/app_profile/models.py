from django.db import models

from exam.my_validators import validate_starts_with_letter, CustomMinLengthValidator


class AppProfile(models.Model):
    nickname = models.CharField(
        max_length=20,
        validators=(
            CustomMinLengthValidator(2),
        ),
        unique=True,
        null=False,
        blank=False,
    )
    first_name = models.CharField(
        max_length=30,
        validators=(
            validate_starts_with_letter,),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=30,
        validators=(
            validate_starts_with_letter,),
        null=False,
        blank=False,
    )
    chef = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )
    bio = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.nickname

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
