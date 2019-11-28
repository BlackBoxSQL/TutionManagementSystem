from django.db import models

# Create your models here.


class Studentregistration(models.Model):
    YEAR_CHOICES = [
        ('1', '1st Year'),
        ('2', '2nd Year'),
    ]
    student_name = models.CharField(max_length=64)
    student_phone = models.CharField(max_length=14)
    guardians_phone = models.CharField(max_length=14)
    college = models.CharField(max_length=64)
    year = models.CharField(max_length=1, choices=YEAR_CHOICES)
    address = models.TextField(max_length=100)

    def __str__(self):
        return self.student_name
