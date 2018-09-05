from django.db import models

class Posts(models.Model):
    author = models.CharField(max_length=5)
