from django.urls import path 
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from EmpRecord import views


app_name = 'Information'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('employee/', views.EmployeeListView.as_view(), name='employee_list'),
    path('employee/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('create/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('employee/<int:pk>/update/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee/<pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
    path('departments/', views.DepartmentListView.as_view(), name='department_list'),
    path('departments/<int:pk>/', views.DepartmentDetailView.as_view(), name='department_detail'),
    path('department/', views.DepartmentCreateView.as_view(), name='department_create'),
    path('department/<int:pk>/update/', views.DepartmentUpdateView.as_view(), name='department_update'),
    path('department/<pk>/delete/', views.DepartmentDeleteView.as_view(), name='department_delete'),
   
]