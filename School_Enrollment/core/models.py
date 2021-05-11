from django.db import models

# Create your models here.


class Student(models.Model):
    student_name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.TextField(blank=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pin = models.CharField(max_length=8)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    class_enrolled = models.CharField(max_length=10)
    marks = models.FloatField()
    enrollment_date = models.DateField()

    def __str__(self):
        return self.student_name.title().strip()
