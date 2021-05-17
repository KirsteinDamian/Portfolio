import datetime

from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        tail = '...' if len(self.body) > 100 else ''
        return self.body[:100] + tail
