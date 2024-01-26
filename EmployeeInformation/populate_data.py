import os
import django
from faker import Faker
import random


# Set up the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EmployeeInformation.settings")
django.setup()


fake = Faker()

def populate(num_records=10):
    from EmpRecord.models import Department, Employee
    for _ in range(num_records):
            name = fake.name()
            designation = fake.name()
            department_obj=fake.name()
            #Course = fake.name()

            department_obj = Department.objects.create(name=fake.name())
                                           
        # Create a Book instance with fake data
            Employee.objects.create(
                name=name,
                designation=designation,
                department=department_obj            # Add other fields as needed
        )

      
if __name__ == '__main__':
    populate(10)
    print("populate successfully")