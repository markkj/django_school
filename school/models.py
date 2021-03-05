from django.db import models
import uuid

class School(models.Model):
    name = models.CharField(max_length=20,blank=False)
    maximum_student = models.IntegerField(default=5)
    address = models.CharField(max_length=255,blank=True,null=True)
    def __str__(self):
        return self.name


class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE,blank=False)
    first_name = models.CharField(max_length=20,blank=False,null=False)
    last_name = models.CharField(max_length=20,blank=False,null=False)
    age = models.IntegerField()
    identification = models.CharField(max_length=36,default=str(uuid.uuid4))

    def __str__(self):
        return self.first_name