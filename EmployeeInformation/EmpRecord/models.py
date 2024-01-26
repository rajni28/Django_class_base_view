from django.db import models
from django.db import models
from django.urls import reverse
# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=256)
   
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("EmpRecord:detail", args=[str(self.pk)])
    

class Employee(models.Model):
    name = models.CharField(max_length=256)
    designation = models.CharField(max_length=256)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("EmpRecord:detail", args=[str(self.pk)])
    