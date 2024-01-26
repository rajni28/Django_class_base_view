from django.urls import path, include 
from .views import DepartmentView, EmployeeView,FilterView
from rest_framework import filters
from rest_framework import routers
# from .views import AuthenticatedView
# from .views import CourseThrottledView
from .views import LoginView, LogoutView
from rest_framework_swagger.views import get_swagger_view

api_router = routers.DefaultRouter(trailing_slash=False)
# api_router.register('student',StudentView)
# api_router.register('course', CourseView)
schema_view = get_swagger_view(title='Employee API: Documentation')

urlpatterns = [ 
    path('', include(api_router.urls)), 
    path('employee_login/', LoginView.as_view()),
    path('employee_logout/', LogoutView.as_view()),
    path('employee/', EmployeeView.as_view(), name="employee_list"),
    path('employee/<int:pk>/', EmployeeView.as_view(), name="employee_detail"),
    path('department/<pk>/', DepartmentView.as_view(), name="department_detail"),
    path('department/', DepartmentView.as_view(), name="department_list"),
    path('api_documentation', schema_view)

]

