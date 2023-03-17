from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import User


class CourseCombinationJamb(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_jamb", blank=True)
    courses = models.CharField(max_length=256, blank=True)

class CourseCombinationWAEC(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_waec", blank=True)
    courses = models.CharField(max_length=256, blank=True)
