from django.db import models
# Create your models here.
class Student(models.Model):
    grade = models.IntegerField()
    class_num = models.IntegerField()
    number = models.IntegerField()
    name = models.CharField(max_length=255)
    def __str__(self):
        return f'grade:{self.grade},class:{self.class_num},number:{self.number},name:{self.name}'
class Homework(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    now_date = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='homework/')