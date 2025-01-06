from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Кастомная модель пользователя"""
    decription = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/')
