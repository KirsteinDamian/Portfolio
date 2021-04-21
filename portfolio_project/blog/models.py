import datetime

from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
