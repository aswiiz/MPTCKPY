from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    established_year = models.IntegerField()
    hod_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
