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


class Payment(models.Model):
    Month_CHOICES = [
        ('jan', 'January'),
        ('feb', 'February'),
        ('mar', 'March'),
        ('apr', 'April'),
        ('may', 'May'),
        ('jun', 'Jun'),
        ('jul', 'July'),
        ('aug', 'August'),
        ('sep', 'September'),
        ('oct', 'October'),
        ('nov', 'November'),
        ('dec', 'December'),
    ]
    student_name = models.ForeignKey(
        Studentregistration, on_delete=models.CASCADE)
    month = models.CharField(max_length=4, choices=Month_CHOICES)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.month
