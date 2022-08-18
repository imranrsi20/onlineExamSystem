from django.db import models
from Writen_Exam.models import *
from django.conf import settings
# Create your models here.


class W_Question(models.Model):
    exam = models.ForeignKey(ExamInfo, on_delete=models.CASCADE)
    question=models.CharField(max_length=200)
    time=models.FloatField(help_text="duration of the quiz in minutes",default=1)



    def __str__(self):
        return str(self.question)

    def get_answers(self):
        return self.w_answer_set.all()


class W_Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True,null=True)
    subject=models.ForeignKey(ExamInfo,on_delete=models.CASCADE,blank=True,null=True)
    question = models.ForeignKey(W_Question, on_delete=models.CASCADE,blank=True,null=True)
    answer=models.CharField(max_length=200)
    mark=models.FloatField(default=0.0,blank=True,null=True)


    def __str__(self):
        return self.mark