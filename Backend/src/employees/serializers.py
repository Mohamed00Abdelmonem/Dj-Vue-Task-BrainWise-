from rest_framework import serializers
from .models import Company, Department, Employee


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'departments_count', 'employees_count']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'company', 'name', 'employees_count']

class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField()  # This will display the department name as a string

    class Meta:
        model = Employee
        fields = [
            'id', 'company', 'role', 'department', 'status', 'name', 'email', 
            'mobile_number', 'address', 'designation', 'hired_on', 'days_employed'
        ]


        