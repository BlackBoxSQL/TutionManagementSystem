from django.db import models
import datetime
# Create your models here.


class Studentregistration(models.Model):
    YEAR_CHOICES = [
        ('1st Year', '1st Year'),
        ('2nd Year', '2nd Year'),
    ]
    student_name = models.CharField(max_length=64)
    student_phone = models.CharField(max_length=14)
    guardians_phone = models.CharField(max_length=14)
    college = models.CharField(max_length=64)
    year = models.CharField(max_length=10, choices=YEAR_CHOICES)
    address = models.TextField(max_length=100)

    def __str__(self):
        return self.id


class Payment(models.Model):
    Month_CHOICES = [
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('Jun', 'Jun'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    ]
    student_name = models.ForeignKey(
        Studentregistration, on_delete=models.CASCADE)
    month = models.CharField(max_length=10, choices=Month_CHOICES)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.student_name


class Attendence(models.Model):
    student = models.ForeignKey(Studentregistration, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    present = models.BooleanField(default=False)

    def __str__(self):
        return self.date


class Result(models.Model):
    student = models.ForeignKey(Studentregistration, on_delete=models.CASCADE)
    batch = models.CharField(max_length=20)
    exam = models.CharField(max_length=20)
    marks = models.CharField(max_length=3)

    def __str__(self):
        return self.batch


class Sheet(models.Model):
    pass
