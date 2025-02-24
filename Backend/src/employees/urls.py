from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  CompanyViewSet, DepartmentViewSet, EmployeeViewSet
from .views import CustomObtainAuthToken



router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', CustomObtainAuthToken.as_view(), name='login'),
    

]