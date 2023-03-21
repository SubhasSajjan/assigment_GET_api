from django.db import models
#from django.contrib.auth.modles import User
# Create your models here.


class department(models.Model):
    dept_id = models.CharField(max_length=20 ,primary_key=True)
    dept_name = models.CharField(max_length=200 ,null=False , default='Aruba')


class employee(models.Model):
    emp_id = models.CharField(max_length=20 , primary_key=True)
    emp_name = models.CharField(max_length=200 ,null=False )
    emp_salary = models.IntegerField(null=False)
    department_id = models.ForeignKey(department , related_name="department_id" , on_delete=models.CASCADE)
