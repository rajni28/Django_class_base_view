from django.shortcuts import render
from django.views.generic import (TemplateView,ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Employee, Department
from django.urls import reverse_lazy
from django.db.models import F, ExpressionWrapper, DecimalField, Value

# Create your views here.

class IndexView(TemplateView):
      template_name = 'index.html'


class EmployeeListView(ListView):
      model = Employee
      template_name = 'employee_list.html'
      context_object_name = 'employee_list' 
      
      # def employee(self, request):
      #       if request is None:
      #             return Employee.objects.none()

           
      
      def get_queryset(self):
         queryset = Employee.objects.select_related('department')
      #all_book = Book.object.all().select_related('publisher').prefetch_related('authors')
      # prefetch_related("authors") also used for Many to Many relationship.
         name_filter = self.request.GET.get('name')
           
         if name_filter:
            queryset = queryset.filter(name__icontains=name_filter)
            order_by = self.request.GET.get('order_by', 'name')
            queryset = queryset.order_by(order_by)

         return queryset

class EmployeeDetailView(DetailView):
      model = Employee
      template_name = 'employee_detail.html'
      context_object_name = 'employee'

class EmployeeCreateView(CreateView):
      fields = ['id', 'name','designation','department']
      model =  Employee
      template_name = 'employee_create_update_form.html'
      success_url = reverse_lazy("EmpRecord:employee_list")

class EmployeeUpdateView(UpdateView):
      fields = ['id', 'name','designation','department']
      model =  Employee
      template_name = 'employee_create_update_form.html'
      success_url = reverse_lazy("EmpRecord:employee_list")

class EmployeeDeleteView(DeleteView):
      model = Employee
      template_name = 'employee_delete.html'
      success_url = reverse_lazy("EmpRecord:employee_list") 

# class EmployeeFilter(FilterView):
#       model = EmployeeFilter
#       template_name = 'filters.html'
#       success_url = reverse_lazy("EmpRecord:employee_list") 
   

class DepartmentListView(ListView):
      model = Department
      template_name = 'department_list.html'
      context_object_name = 'department_list'

      def get_queryset(self):
         queryset = Department.objects.all()
         name_filter = self.request.GET.get('name')
           
         if name_filter:
            queryset = queryset.filter(name__icontains=name_filter)
            order_by = self.request.GET.get('order_by', 'name')
            queryset = queryset.order_by(order_by)
         return queryset
    
   
class DepartmentDetailView(DetailView):
      model = Department
      template_name = 'department_detail.html'
      context_object_name = 'department'

class DepartmentCreateView(CreateView):
      fields = ['id', 'name']
      model = Department
      template_name = 'department_create_update_form.html'
      success_url = reverse_lazy("EmpRecord:department_list")

class DepartmentUpdateView(UpdateView):
      fields = ['id', 'name']
      model = Department
      template_name = 'department_create_update_form.html'
      success_url = reverse_lazy("EmpRecord:department_list")

class DepartmentDeleteView(DeleteView):
      model =  Department
      template_name = 'department_delete.html'
      success_url = reverse_lazy("EmpRecord:department_list") 
       

# optimising is one of the technique and also Caching is used for optimising. 