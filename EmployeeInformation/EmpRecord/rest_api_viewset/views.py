from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import viewsets
from .serializers_api import DepartmentSerializer, EmployeeSerializer
from rest_framework.decorators import action
from django.db.models import Prefetch
from EmpRecord.models import Department, Employee
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import action


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
       
    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.serializer_class
        elif self.action == "department":
            return DepartmentSerializer
        elif self.action == "department/1/HR":
            return DepartmentSerializer
        else:
            return self.serializer_class

    def retrieve(self, request, pk=None):
        department = self.get_object()
        serializer = self.get_serializer(department)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=["get"])
    def get_employee_data(self, request, pk=None):
        print('>>>pk',pk)
        department_employees = Employee.objects.filter(department_id=pk)
        serializer = EmployeeSerializer(department_employees, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
   
    @action(detail=False, methods=["get"])
    def get_hr_list(self, request, pk=None):
        department = Department.objects.filter(name__iexact='hr')
        serializer = self.get_serializer(department, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


    def retrieve(self, request, pk=None):
        employee = self.get_object()
        serializer = self.get_serializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["get"])
    def get_employee_data(self, request, pk=None):
        designation = Employee.objects.filter(designation=pk)
        serializer = EmployeeSerializer(designation, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"])
    def get_employee_name(self, request, pk=None):
        employee = Employee.objects.filter(name__iexact='B')
        serializer = self.get_serializer(employee, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

