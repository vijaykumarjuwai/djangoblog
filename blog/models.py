from django.db import models
from django.utils import timezone

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self)\
                .get_queryset().filter(status='published')

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    post_date = models.DateTimeField('date published')
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
