

# from django.conf import settings
from django.contrib.auth.models import AbstractUser

from django.db import models
# from django.utils import timezone


class User(AbstractUser):
    INVALID_CODE = "######"
    avatar = models.ImageField(upload_to="user/", null=True, blank=True)

    full_name = models.CharField(("full name"), max_length=256)
    email = models.EmailField(
        ("email"),
        unique=True,
        error_messages={
            "error": ("Bunday email mavjud."),
        },
        null=True
    )
    
    created_at = models.DateTimeField(("date created"), auto_now_add=True, null=True)
    updated_at = models.DateTimeField(("date updated"), auto_now=True)

    # SETTINGS
    USERNAME_FIELD = "email"
    first_name = None
    last_name = None
    REQUIRED_FIELDS = ["username", "full_name"]

    def __str__(self):
        return f"{self.email}"

    class Meta:
        db_table = "user"
        swappable = "AUTH_USER_MODEL"
        verbose_name = ("user")
        verbose_name_plural = ("users")
