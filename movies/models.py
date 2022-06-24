from django.db import models
from django.template.defaultfilters import slugify
from uuid import uuid4

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.ManyToManyField(Genre, related_name="moviegenre", blank=True, null=True)
    slug = models.CharField(max_length=200, null=False)
    image = models.ImageField(upload_to="Cover Images", null=True)
    file = models.FileField(upload_to="Video", null=True)
    created = models.DateField(null=False, blank=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify('{} {}'.format(self.title, str(uuid4())))
        super(Movie, self).save(*args, **kwargs)