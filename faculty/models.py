from django.db import models
from departments.models import Department

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='faculties')
    designation = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    email = models.EmailField()
    image = models.ImageField(upload_to='faculty/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.designation}"
