from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(
        self, email, password, is_staff, is_superuser, is_admin, **extra_fields
    ):
        if not email:
            raise ValueError("Users must have an email address")
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            is_admin=is_admin,
            last_login=now,
            date_joined=now,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, True, **extra_fields)
        user.save(using=self._db)
        return user

    def create_admin(self, email, password, **extra_fields):
        user = self._create_user(
            email=email,
            password=password,
            is_staff=False,
            is_superuser=False,
            is_admin=True,
            **extra_fields,
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=300)
    username = models.CharField(max_length=254, blank=False, unique=True)
    first_name = models.CharField(max_length=256, blank=True)
    last_name = models.CharField(max_length=256, blank=True)
    career_choice = models.CharField(max_length=256, blank=True, null=True)
    educational_level = models.CharField(max_length=256, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_child_node = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]

    objects = UserManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip()


class CourseCombinationJamb(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_jamb", blank=True)
    courses = models.CharField(max_length=256, blank=True)

class CourseCombinationWAEC(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_waec", blank=True)
    courses = models.CharField(max_length=256, blank=True)
