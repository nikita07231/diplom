from django.db import models


class Block(models.Model):
    title = models.CharField(max_length=200)
    image_auto = models.BooleanField()
    image_bus = models.BooleanField()
    price = models.CharField(max_length=100, blank=True)
