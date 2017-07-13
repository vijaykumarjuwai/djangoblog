from django.db import models
from django.utils import timezone

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    post_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title
