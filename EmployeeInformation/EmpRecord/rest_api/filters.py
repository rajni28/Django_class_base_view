import django_filters
from EmpRecord.models import Employee


class EmployeeFilter(django_filters.FilterSet):
    name= django_filters.CharFilter(lookup_expr='iexact')
    
    
    class Meta:
        model = Employee
        fields = ("name", "designation", "department")