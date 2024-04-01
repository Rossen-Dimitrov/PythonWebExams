from django.core.validators import MinLengthValidator
from django.db import models
from fruitipedia_app.my_validators import validate_only_letters


class Fruit(models.Model):
    FRUIT_NAME_MAX_LENGTH = 30
    FRUIT_NAME_MIN_LENGTH = 2
    name = models.CharField(
        max_length=FRUIT_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(FRUIT_NAME_MIN_LENGTH),
            validate_only_letters
        ]
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    nutrition = models.TextField(
        null=True,
        blank=True,
    )
