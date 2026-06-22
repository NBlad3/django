from django.db import models

class Student(models.Model):
  name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  gender = models.CharField(max_length=255)
  age = models.IntegerField(default=0)