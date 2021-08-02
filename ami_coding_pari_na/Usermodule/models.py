from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(
        ('username'),
        max_length=150,
        unique=True,
        help_text=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': ("A user with that username already exists."),
        },
    )
    contact_no = models.BigIntegerField(unique=True, default=None, null=True, blank=True)
    REQUIRED_FIELDS=['email',]
    def __str__(self):
        return self.username



