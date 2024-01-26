from django.urls import path,include
from .views import EmployeeListView, DepartmentListView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('employee_list/', EmployeeListView.as_view(), name='employee-list-create'),
    path('employee_list/<int:id>/', EmployeeListView.as_view(), name='employee-list-create'),
    path('department_list/',DepartmentListView.as_view(), name='department-list-create'),
    path('department_list/<int:id>/', DepartmentListView.as_view(), name='department-list-create'),
    
]