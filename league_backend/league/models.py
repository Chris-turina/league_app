from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __self__(self):
        return self.email






class League(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.name