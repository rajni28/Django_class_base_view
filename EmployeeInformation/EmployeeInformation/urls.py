"""EmployeeInformation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp_records/', include(('EmpRecord.urls'), namespace='EmpRecord')),
    path('rest_api/', include(('EmpRecord.rest_api.urls', 'EmpRecord_api'),
                                    namespace='rest_api')),
    path('rest_api_viewset/', include(('EmpRecord.rest_api_viewset.urls', 'EmpRecord_api'),
                                    namespace='rest_api_viewset')),                                
    path('rest_api_genericset/', include(('EmpRecord.rest_api_genericset.urls', 'EmpRecord_api'),
                                    namespace='rest_api_genericset')),
    path('postmans/', include(('EmpRecord.Postman_Hardik.urls'))),
    path('hrdik_Cls_bsd_API/', include(('EmpRecord.Hrdik_Cls_bsd_API.urls'))),
    path('hrdik_gnric_API/', include(('EmpRecord.Hrdik_gnric_API.urls'))),                                                              
    path('__debug__/', include(debug_toolbar.urls)),
 ]                               
 

