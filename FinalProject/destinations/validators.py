from django.core.validators import ValidationError


def validate_location(value):
    for sym in value:
        if not sym.isalpha() and sym != ' ':
            raise ValidationError("Only letters and spaces allowed")
