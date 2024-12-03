from django.db import models

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=50)
    age = models.IntegerField()
    date_of_enrollment = models.DateField()

    def __str__(self):
        return self.name
