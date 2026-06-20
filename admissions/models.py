from django.db import models

class AdmissionEnquiry(models.Model):
    student_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    course_interested = models.CharField(max_length=100)
    message = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Reviewed', 'Reviewed')], default='Pending')

    def __str__(self):
        return f"{self.student_name} - {self.course_interested}"
