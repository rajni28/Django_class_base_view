from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404
from .pagination import CustomPagination
from .serializers import DepartmentSerializer, EmployeeSerializer
from EmpRecord.models import Department, Employee
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django_filters.views import FilterView
from django.contrib.auth import login as django_login, logout as django_logout 
from rest_framework.authtoken.models import Token  
from .serializers import LoginSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import FilterSet 
from django_filters.rest_framework import  filters

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)
    

class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response(status=204)
    
class DepartmentView(APIView):
    pagination_class = CustomPagination
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated] 
    
    def get(self, request, pk=None):
        user = request.user
        serializers = DepartmentSerializer(data=request.data)

        if pk:
            queryset =  get_object_or_404(Department, pk=pk) 
            serializers = DepartmentSerializer(queryset)
        else:
            queryset = Department.objects.all()
            serializers = DepartmentSerializer(queryset, many=True)
            paginator = self.pagination_class()
            result_page = paginator.paginate_queryset(queryset, request)
            serializers = DepartmentSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializers.data)
        return Response(serializers.data)
         
    def post(self, request):
         serializer = DepartmentSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        serializers = DepartmentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        try:
            department = Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            return Response({"error": "Department not found"}, status=status.HTTP_404_NOT_FOUND)
        department.delete()
        return Response({"message": "Department deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class EmployeeFilter(FilterSet):
    designation = filters.CharFilter(method='filter_by_designation')
    # min_salary = filters.CharFilter(method="filter_by_min_salary")
    # max_salary = filters.CharFilter(method="filter_by_max_salary")


    class Meta:
        model = Employee
        fields = ('name', 'designation','department')
    
    def filter_by_designation(self, queryset, name, value):
        designation = value.strip().split('-')
        designation = designation.objects.filter(name_in=designation)
        return queryset.filter(designation_in=designation)
    
    # def filter_by_min_salary(self, queryset, name, value):
    #     queryset = queryset.filter(salary_gt=value)
    #     return queryset

    # def filter_by_max_salary(self, queryset, name, value):
    #     queryset = queryset.filter(salary_lt=value)
    #     return queryset
        


class EmployeeView(APIView):
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated] 
    # filter_backends = (DjangoFilterBackend)
    # filter_fields = ( 'name','designation','department')
    filter_backends = (DjangoFilterBackend,OrderingFilter, SearchFilter)
    filter_class = EmployeeFilter
    ordering_fields = ('[designation]')
    ordering = ('name') 
    search_fields = ('name','designation')
    
   
    def get(self, request, pk=None):
        user = request.user
        serializers = EmployeeSerializer(data=request.data)
        if pk:
            instance = Employee.objects.get(pk=pk)
            serializers = EmployeeSerializer(instance)
        else:
            queryset = Employee.objects.all()
            serializers = EmployeeSerializer(queryset, many=True)
            paginator = self.pagination_class()
            result_page = paginator.paginate_queryset(queryset, request)
            serializers = EmployeeSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializers.data)
            
        return Response(serializers.data)

    def get_queryset(self):
        query_set = self.filter_queryset(Employee.objects.all())
        return query_set

    def post(self, request):
        serializers = EmployeeSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        serializers = EmployeeSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
           return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        employee.delete()
        return Response({"message": "Employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        
        
      
        
        


    
   




