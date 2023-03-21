from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from central_details.models import *
from django.db.models import Max

# Create your views here.
@api_view(['GET' , 'POST' , 'PUT' , 'DELETE'])
def department_list(request):
    if request.method == 'GET':
        departments =department.objects.all()
        list1 = DepartmentSerializer(departments, many = True)
        return Response(list1.data)


@api_view(['GET' , 'POST' , 'PUT' , 'DELETE'])
def employee_list(request):
    if request.method == 'GET':
        # emps = employee.objects.all()
        # sites = EmployeeSerializer(emps , many = True)
        departments= employee.objects.values('department_id').distinct()
        print(departments)

        thisList = []
        for department in departments:
            high_sal_emp = employee.objects.filter(department_id = department['department_id']).order_by('-emp_salary').first()
            print(high_sal_emp)
            thisList.append(
                {
                'department':department['department_id'],
                'Highest_salary_employee_name':high_sal_emp.emp_name,
                'Highest_salary_employee_id':high_sal_emp.emp_id,
                'salary':high_sal_emp.emp_salary

                }
            )
        
            
        #return Response(sites.data)
        return Response(thisList)