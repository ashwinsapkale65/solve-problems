from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser

COLOR_CHOICES = (
    ('student','STUDENT'),
    ('teacher', 'TEACHER')
)


# Create your models here.

class User(AbstractUser):
    registeras = models.CharField(max_length=10, choices=COLOR_CHOICES, default='green')



class studentregistrations(models.Model):
    username = models.CharField(max_length=122)
  
    name  =  models.CharField(max_length=122)
    class1 = models.CharField(max_length=122)
    div = models.CharField(max_length=122)
    roll = models.CharField(max_length=122)
    contact= models.CharField(max_length=20)


    def __str__(self):
        return self.username

class teacherregistrations(models.Model):
    username = models.CharField(max_length=122)
    
    name  =  models.CharField(max_length=122)
    class1 = models.CharField(max_length=122)
    div = models.CharField(max_length=122)
    
    contact= models.CharField(max_length=20)


    def __str__(self):
        return self.username


class checkstudent(models.Model):
    username = models.CharField(max_length=122)
    
    check_type = models.CharField(max_length=22)

    def __str__(self):
        return self.username
  

