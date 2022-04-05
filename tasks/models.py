from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=512)
