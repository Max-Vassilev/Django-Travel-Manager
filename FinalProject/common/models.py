from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

UserModel = get_user_model()


class Post(models.Model):
    location = models.CharField(max_length=25, validators=[MinLengthValidator(2), ])
    image_url = models.URLField(max_length=300)
    post_information = models.CharField(max_length=150, null=True, blank=True)

    posted_by_user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
