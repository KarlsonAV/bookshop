from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models


class CustomUser(AbstractUser):
    paid_books = ArrayField(models.CharField(max_length=200), blank=True, default=list)
