from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100, blank=True)
    roll_number = models.CharField(max_length=20, blank=True)
    age = models.IntegerField(default=0, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='students')

    # Add more fields as needed

class Teacher(models.Model):
    name = models.CharField(max_length=100, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teachers')

    # Add more fields as needed
