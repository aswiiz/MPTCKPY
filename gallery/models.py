from django.db import models

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    date_added = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
