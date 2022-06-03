from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="Cover Images", null=True)
    file = models.FileField(upload_to="Video", null=True)
    created = models.DateField(null=False, blank=False, auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title