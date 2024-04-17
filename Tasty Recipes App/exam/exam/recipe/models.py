from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


class Recipe(models.Model):
    CHOICES = (
        ("French", "French"),
        ("Chinese", "Chinese"),
        ("Italian", "Italian"),
        ("Balkan", "Balkan"),
        ("Other", "Other"),
    )

    title = models.CharField(
        unique=True,
        max_length=100,
        validators=[MinLengthValidator(10)],
        null=False,
        blank=False,
    )
    cuisine_type = models.CharField(
        max_length=7,
        choices=CHOICES,
    )
    ingredients = models.TextField(
        null=False,
        blank=False,
        help_text="Ingredients must be separated by a comma and space."
    )

    instructions = models.TextField(
        null=False,
        blank=False,
    )
    cooking_time = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Provide the cooking time in minutes.",
        null=False,
        blank=False,
    )
    image_url = models.URLField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title
