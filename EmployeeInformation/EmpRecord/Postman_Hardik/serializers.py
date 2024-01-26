from rest_framework import serializers
from EmpRecord.models import Department, Employee

class DepartmentSerializer(serializers.ModelSerializer):
   
    class Meta:
        fields =['id', 'name']
        model = Department


    # def get_department(self, obj):
    #     serializers =DepartmentSerializer(
    #     department_obj=obj.department.all(), many=True)
    #     return serializers.data

   
    
    
class EmployeeSerializer(serializers.ModelSerializer):
    # department = DepartmentSerializer()

    class Meta:
        fields =['id','name', 'designation', 'department']
        model = Employee

