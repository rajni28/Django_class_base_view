from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import  DepartmentViewSet, EmployeeViewSet

router = DefaultRouter()
router.register('employees', EmployeeViewSet, basename='employee')
router.register('departments', DepartmentViewSet, basename= 'department')

urlpatterns = [
    # path('employee', EmployeeViewSet.as_view({'get': 'list'}), name="employee_list"),
    # path('department', DepartmentViewSet.as_view({'get': 'list'}), name="department_list"),
    path('employee/', include(router.urls)),
    path('department/', include(router.urls)),
]