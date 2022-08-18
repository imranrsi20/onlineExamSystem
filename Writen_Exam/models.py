from django.db import models
from django.conf import settings
import random
# Create your models here.


class ExamInfo(models.Model):
    subject=models.CharField(max_length=120)
    topic=models.CharField(max_length=120)
    number_of_questions=models.IntegerField()
    required_score_to_pass=models.IntegerField(help_text="required score in %")
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.subject

    def get_questions(self):
        questions=list(self.w_question_set.all())
        return questions






class W_Result(models.Model):
    exam=models.ForeignKey(ExamInfo,on_delete=models.CASCADE,blank=True,null=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100,blank=True,null=True)
    student_id = models.CharField(max_length=50,blank=True,null=True)
    score=models.FloatField()

    def __str__(self):
        return self.student_id