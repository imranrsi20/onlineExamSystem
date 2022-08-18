from django.db import models
from quizes.models import *
from django.conf import settings
from django.contrib.auth.models import User
from accounts.models import *
# Create your models here.

class Result(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,blank=True,null=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100,blank=True,null=True)
    Student_id = models.CharField(max_length=50,blank=True,null=True)
    score=models.FloatField()

    def __str__(self):
        return str(self.pk)