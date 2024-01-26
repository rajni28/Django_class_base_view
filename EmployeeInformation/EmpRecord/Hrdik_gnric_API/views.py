from rest_framework import generics, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.db.models import Prefetch
from EmpRecord.models import Employee, Department
from .serializers import DepartmentSerializer, EmployeeSerializer


class EmployeeListView(generics.GenericAPIView, 
                       mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin):
    
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    lookup_field = "id"

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id) 
        else:
            return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def perform_create(self, serializer):
        serializer.save(Department=self.request.user)  
    
    def put(self, request, id=None):
        return self.update(request, id)
    
    def delete(self, request, id=None):
        return self.destroy(request, id)
    
class DepartmentListView(generics.GenericAPIView, 
                       mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    lookup_field = 'id'

    def get(self, request):
        if id:
            return self.retrieve(request, id) 
        else:
            return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def put(self, request, id=None):
        return self.update(request, id)