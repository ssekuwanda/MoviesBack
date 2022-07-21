from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from uuid import uuid4

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.ManyToManyField(Genre, related_name="moviegenre")
    slug = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to="Cover Images", null=True)
    file = models.FileField(upload_to="Video", null=True)
    created = models.DateField(null=False, blank=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify('{} {}'.format(self.title, str(uuid4())))
        super(Movie, self).save(*args, **kwargs)

class Downloaded(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    movie = models.ManyToManyField(Movie, related_name='my_movies', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class QrCodePayment(models.Model):
    code = models.CharField(max_length=120, blank=False, null=False)
    user = models.ForeignKey(User, related_name='payer', on_delete=models.CASCADE)
    creator = models.ForeignKey(User, related_name='issuer', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    used = models.BooleanField(default=False)

    def __str__(self):
        return self.code

    def save(self):
        pass

    