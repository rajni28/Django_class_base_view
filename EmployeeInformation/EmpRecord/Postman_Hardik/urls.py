from django.urls import path 
from EmpRecord.views import *
# from EmpRecord import views
from .views import  EmployeeListView, EmployeeDetailView


app_name = 'EmployeeInformation'

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('employee_list_test/', EmployeeListView, name='employee_list'),
    path('employee_list_test/<int:pk>/', EmployeeDetailView, name='employee_detail'),
   
]