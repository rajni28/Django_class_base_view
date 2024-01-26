from rest_framework import serializers
from EmpRecord.models import Department, Employee


class DepartmentSerializer(serializers.ModelSerializer):
   
    class Meta:
        fields = "__all__"
        model = Department


    def get_department(self, obj):
        serializers =DepartmentSerializer(
        department_obj=obj.department.all(), many=True)
        return serializers.data

   
    
    
class EmployeeSerializer(serializers.ModelSerializer):
    # department = DepartmentSerializer()

    class Meta:
        fields = "__all__"
        model = Employee


    def get_employee(self, obj):
        serializers =EmployeeSerializer(
        employee_obj=obj.employee.all(), many=True)
        return serializers.data
