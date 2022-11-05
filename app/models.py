import uuid

from django.db import models


# Create your models here.
class Todos(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title 