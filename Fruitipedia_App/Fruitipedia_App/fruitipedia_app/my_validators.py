from django.core import exceptions


def validate_starts_with_letter(value):
    if not value[0].isalpha():
        raise exceptions.ValidationError("Your name must start with a letter!")


def validate_only_letters(value):
    if not value.isalpha():
        raise exceptions.ValidationError("Fruit name should contain only letters!")
