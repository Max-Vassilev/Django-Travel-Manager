from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinLengthValidator

UserModel = get_user_model()


class VisitedPlace(models.Model):
    location = models.CharField(max_length=30, validators=[MinLengthValidator(2), ])
    place_photo = models.URLField()

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
