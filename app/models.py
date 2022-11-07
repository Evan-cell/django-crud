import uuid

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Todos(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    def __str__(self):
        return self.title 