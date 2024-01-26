from django.shortcuts import render, reverse 
from rest_framework.parsers import JSONParser
from EmpRecord.models import Employee, Department
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F, ExpressionWrapper, DecimalField, Value
from rest_framework.parsers import JSONParser 
from django.http import Http404, HttpResponse, JsonResponse
from .serializers import DepartmentSerializer, EmployeeSerializer
from django.utils.decorators import method_decorator



@csrf_exempt
def EmployeeListView(request):
    if request.method == 'GET':
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many= True)
        return JsonResponse(serializer.data, safe= False)
    
    elif request.method == 'POST':
        Json_parser = JSONParser()
        data = Json_parser.parse(request)
        serializer = EmployeeSerializer(data= data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.erros, status=400)
    

@csrf_exempt
def EmployeeDetailView(request):
    try:
        instance = Employee.objects.all()
    except Employee.DoesNotExist as e:
        return JsonResponse( {"error": "Given employee object not found."}, status=404)

    if request.method == 'GET':
        serializer = EmployeeSerializer(instance)
        return JsonResponse(serializer.data)
    
    elif request.method == "PUT":
        Json_parser = JSONParser()
        data = Json_parser.parse(request.PUT)
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
       instance.delete()
       return HttpResponse(status=204)
    