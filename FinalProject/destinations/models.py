from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinLengthValidator

from FinalProject.destinations.validators import validate_location

UserModel = get_user_model()


class DreamDestination(models.Model):
    location = models.CharField(max_length=30, validators=[MinLengthValidator(2), validate_location])
    place_photo = models.URLField()

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
