from django.core import exceptions
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _


def validate_starts_with_letter(value):
    if not value[0].isalpha():
        raise exceptions.ValidationError("Name must start with a capital letter!")


class CustomMinLengthValidator(MinLengthValidator):
    message = _("Nickname must be at least 2 characters long!")
