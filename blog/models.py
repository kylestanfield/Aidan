from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Image(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    height = models.IntegerField()
    width = models.IntegerField()

    def __str__(self):
        return self.title
