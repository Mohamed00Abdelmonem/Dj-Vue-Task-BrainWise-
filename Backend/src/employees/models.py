from django.db import models



class UserAccount(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    )
    user_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.user_name


class Company(models.Model):
    name = models.CharField(max_length=255)
    departments_count = models.PositiveIntegerField(default=0)
    employees_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='departments')
    name = models.CharField(max_length=255)
    employees_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.company.name} - {self.name}"



ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    )

class Employee(models.Model):
    STATUS_CHOICES = (
        ('application_received', 'Application Received'),
        ('interview_scheduled', 'Interview Scheduled'),
        ('hired', 'Hired'),
        ('not_accepted', 'Not Accepted'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='application_received')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    address = models.TextField(blank=True)
    designation = models.CharField(max_length=255, blank=True)
    hired_on = models.DateField(null=True, blank=True)
    days_employed = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.status == 'hired' and self.hired_on:
            from datetime import date
            self.days_employed = (date.today() - self.hired_on).days
        super(Employee, self).save(*args, **kwargs)

    def __str__(self):
        return self.name