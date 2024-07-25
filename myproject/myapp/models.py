from django.db import models
from django.utils import timezone

# Create your models here.

class University(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
