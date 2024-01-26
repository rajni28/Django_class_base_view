from django.urls import path, include 
from .views import EmployeeAPIView, EmployeeDetailAPIView
from rest_framework import routers
# from .views import AuthenticatedView
# from .views import CourseThrottledView
from EmpRecord.views import *



api_router = routers.DefaultRouter(trailing_slash=False)
# api_router.register('student',StudentView)
# api_router.register('course', CourseView)

urlpatterns = [ 
    path('', include(api_router.urls)), 
    path('employees_api/', EmployeeAPIView.as_view(), name="employee_api"),
    path('employees_api_detail/<int:id>/', EmployeeDetailAPIView.as_view(), name="employee_api_detail"),
    # path('department/<pk>/', DepartmentView.as_view(), name="department_detail"),
    # path('department/', DepartmentView.as_view(), name="department_list"),
] 

