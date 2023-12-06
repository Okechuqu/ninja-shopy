from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
# from plugins.code_generator import generateUniqueId

# Create your models here.


class CustomUserManager(UserManager):
    def _create_user(self, username, password, email, **extra_fields):
        if not email:
            raise ValueError("You have not provided a vaild email address")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, password=None, username=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(
        self, username=None, email=None, password=None, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(username, password, email, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    # DEFAULT FIELD
    email = models.EmailField(("email address"), unique=True)
    password = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(
        max_length=200, null=False, blank=False, unique=True)

    first_name = models.CharField(max_length=300, null=True, blank=True)
    last_name = models.CharField(max_length=300, null=True, blank=True)
    phone = models.CharField(max_length=300, null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # section for mananging api session login
    # code = models.CharField(max_length=10, unique=True, default=generateUniqueId, editable=False)
    # token = models.CharField(max_length=600, blank=True, null=True)
    # key = models.CharField(max_length=150, blank=True, null=True)
    # is_token_verified = models.BooleanField(default=False)
    # isPassRequest = models.BooleanField(default=False)

    # otp = models.CharField(max_length=6, blank=True, null=True)
    # is_verified = models.BooleanField(default=False)
    # otp_created_at = models.DateTimeField(null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def _str_(self):
        return self.username
