from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Slide(models.Model):
    description = models.CharField(max_length=200)
    filename = models.CharField(max_length=200)
    height = models.IntegerField()
    width = models.IntegerField()
    id_num = models.IntegerField()

    def __str__(self):
        return self.title
