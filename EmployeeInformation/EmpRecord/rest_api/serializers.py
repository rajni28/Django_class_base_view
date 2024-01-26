from rest_framework import serializers
from EmpRecord.models import Department, Employee
from rest_framework import exceptions 
from django.contrib.auth import authenticate


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username', "")
        password = data.get('password', "")  

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "User is deactivated."
                    raise exceptions.validationError(msg)
            else:
                    msg = "Unable to login with given credentials."
                    raise exceptions.validationError(msg)
        else:
            msg = "Must provide username and password both"
            raise exceptions.validationError(msg)
        return data



class DepartmentSerializer(serializers.ModelSerializer):
   
    class Meta:
        fields =['id', 'name']
        model = Department


    def get_department(self, obj):
        serializers =DepartmentSerializer(
        department_obj=obj.department.all(), many=True)
        return serializers.data

   
    
    
class EmployeeSerializer(serializers.ModelSerializer):
    # department = DepartmentSerializer()

    class Meta:
        fields =['id','name', 'designation', 'department']
        model = Employee
        depth=1


    def get_employee(self, obj):
        serializers =EmployeeSerializer(
        employee_obj=obj.employee.all(), many=True)
        return serializers.data
