from django.shortcuts import render, reverse, get_object_or_404
from rest_framework.parsers import JSONParser
from EmpRecord.models import Employee, Department
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F, ExpressionWrapper, DecimalField, Value
from rest_framework.parsers import JSONParser 
from django.http import Http404, HttpResponse, JsonResponse
from .serializerss import EmployeeSerializer
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from EmpRecord.views import *




class EmployeeAPIView(APIView):
    def get(self, request):
        employee = Employee.objects.all()
        serializers = EmployeeSerializer(employee, many=True)
        return Response(serializers.data, status=200)
    
    def post(self, request):
        data = request.data
        serializers = EmployeeSerializer(data= data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=201)
        return Response(serializers.erros, status=400)
    
class EmployeeDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return Employee.objects.get(id=id)
        except Employee.DoesNotExist as e:
            return None
        
    def get(self, request, id=None):
        instance = self.get_object(id)
        if not instance:
            return Response( {"error": "Given Employee object not found. "}, status= 404)
        serializers = EmployeeSerializer(instance)
        return Response(serializers.data, status=200)
    
    def put(self, request, id=None):
        data = request.data
        instance = self.get_object(id)
        serializers = EmployeeSerializer(instance, data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=200)
        return Response(serializers.errors, status=400)
    
    def delete(self, request, id=None):
        instance = self.get_object(id)
        if not instance:
            return Response( {"error": "Given Employee object not found. "}, status= 404)
        instance.delete()
        return HttpResponse()
        