from django.db import models

# Create your models here.
class Task(models.Model):
    tname=models.CharField(max_length=300)
    tpriority=models.IntegerField()
    tdate=models.DateField()

    def __str__(self):
        return self.tname



