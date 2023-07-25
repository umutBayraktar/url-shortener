from django.db import models

class URLItem(models.Model):
    reference = models.CharField(unique=True, primary_key=True, max_length=10)
    url = models.URLField()
