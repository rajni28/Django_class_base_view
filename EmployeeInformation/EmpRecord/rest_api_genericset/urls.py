from django.urls import path,include
from .views import EmployeeListCreateAPIView, EmployeeRetrieveUpdateDestroyAPIView
from .views import DepartmentListCreateAPIView
from.views import DepartmentRetrieveUpdateAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('employees', EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
    path('employees', EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employee-detail'),
    path('departments', DepartmentListCreateAPIView.as_view(), name='department-list-create'),
    path('departments', DepartmentRetrieveUpdateAPIView.as_view(), name='department-detail'),

]