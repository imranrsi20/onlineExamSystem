from django.db import models

# Create your models here.

class Evaluate(models.Model):
    user = models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    question=models.CharField(max_length=250)
    answer=models.TextField()
    mark=models.FloatField(default=0.0)

    def __str__(self):
        return self.user


