from django.core.validators import MinValueValidator
from django.db import models


class Album(models.Model):
    MAX_ALBUM_NAME_LENGTH = 30
    CHOICES = (
        ("POP", "Pop Music"),
        ("JAZZ", "Jazz Music"),
        ("R&B", "R&B Music"),
        ("ROCK", "Rock Music"),
        ("COUNTRY", "Country Music"),
        ("DANCE", "Dance Music"),
        ("HIPHOP", "Hip Hop Music"),
        ("OTHER", "Other"),
    )
    album_name = models.CharField(
        max_length=MAX_ALBUM_NAME_LENGTH,
        unique=True,
        blank=False,
        null=False,
    )
    artist_name = models.CharField(
        max_length=MAX_ALBUM_NAME_LENGTH,
        blank=False,
        null=False,
    )
    genre = models.CharField(
        max_length=MAX_ALBUM_NAME_LENGTH,
        blank=False,
        null=False,
        choices=CHOICES
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    image_url = models.URLField(
        blank=False,
        null=True,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False,
        validators=(
            MinValueValidator(0.0),
        ),
    )
