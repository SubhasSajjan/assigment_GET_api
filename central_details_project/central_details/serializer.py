from rest_framework import serializers , response
from .models import *

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = department
        fields =['dept_id' , 'dept_name']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields =["emp_id" , "emp_name" , "emp_salary" , "department_id"]