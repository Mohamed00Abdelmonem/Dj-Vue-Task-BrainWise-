from django.contrib import admin
from .models import Company, Department, Employee, UserAccount


admin.site.register(Company)
admin.site.register(UserAccount)
admin.site.register(Department)
admin.site.register(Employee)
# Register your models here.
