from django.db import models


class Expense(models.Model):
    MAX_TITLE_LENGTH = 30
    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        blank=False,
        null=False,
    )
    expense_image = models.URLField(
        blank=False,
        null=False,
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    price = models.FloatField(
        blank=False,
        null=False
    )
