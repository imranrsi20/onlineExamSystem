from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Student(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    name =models.CharField(max_length=50)
    student_id = models.CharField(max_length=100)

    def __str__(self):
        return self.student_id


class Teacher(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    designation = models.CharField(max_length=100)
    teacher_id = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.teacher_id