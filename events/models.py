from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateTimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/', blank=True, null=True)

    def __str__(self):
        return self.title
