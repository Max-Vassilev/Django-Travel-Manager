from django.db import models
from django.core.validators import MinLengthValidator

from django.contrib.auth import models as auth_models


class TravelUser(auth_models.AbstractUser):
    first_name = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(2), ],
    )

    last_name = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(2), ],
    )

    email = models.EmailField(unique=True)
