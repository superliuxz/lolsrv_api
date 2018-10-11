from django.db import models


class Images(models.Model):
    repo = models.CharField(max_length=100)
    date = models.DateTimeField()
    sha = models.CharField(max_length=11, primary_key=True)
    img = models.BinaryField()
