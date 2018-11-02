from django.db import models

# Create your models here.
class Poem(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # author

    def __str__(self):
        return self.title
