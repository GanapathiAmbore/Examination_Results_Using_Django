from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=20)
    group=models.CharField(max_length=10,choices=(('M.P.C','M.P.C'),('Bi.P.C','Bi.P.C'),('C.E.C','C.E.C')))
    year=models.DateField()
    grade=models.CharField(max_length=1,choices=(('A','first'),('B','second'),('C','third')))
    credits=models.IntegerField()
    image=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name

class Hallticket(models.Model):
    student=models.OneToOneField(Student,on_delete=models.CASCADE,primary_key=True)
    no=models.IntegerField()

    def __str__(self):
        return str(self.no)

