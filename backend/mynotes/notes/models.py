from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Note(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.body[:50]