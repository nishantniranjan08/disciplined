import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(unique=False, blank=False, null=False) #Make this field unique after development

    def __str__(self):
        return self.username
