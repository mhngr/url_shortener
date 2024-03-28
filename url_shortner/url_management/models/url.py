from django.db import models


class Url(models.Model):
    username = models.CharField(max_length=100)
    long_url = models.CharField(max_length=1000)
    short_url = models.CharField(max_length=10, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100)
