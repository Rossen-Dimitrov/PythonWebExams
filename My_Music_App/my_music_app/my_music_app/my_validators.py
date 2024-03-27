from django.core import exceptions


def verify_only_letters_numbers_and_underscore(value):
    for char in value:
        if not char.isalnum() and not char == '_':
            raise exceptions.ValidationError("Ensure this value contains only letters, numbers, and underscore.")
