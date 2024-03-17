from django.db import models


class Url(models.Model):
    long_url = models.CharField(max_length=1000)
    short_url = models.CharField(max_length=10, null=True, blank=True)
    username = models.CharField(max_length=100)
    category = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100)
