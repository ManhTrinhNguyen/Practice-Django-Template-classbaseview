from django.urls import path 
from . import views 


urlpatterns = [
  path('home/', views.HomeView.as_view()),
  path('about/', views.about),
  path('menu/', views.menu),
  path('employees/create/', views.EmployeeCreate.as_view(), name = 'EmployeeCreate'),
  path('employees/list', views.EmployeeList.as_view(), name = 'EmployeeList'),
  path('employees/detail/<int:pk>', views.EmployeeDetail.as_view(), name = 'EmployeeDetail'),
  path('employees/update/<int:pk>', views.EmployeeUpdate.as_view(), name = 'EmployeeUpdate'),
  path('employees/delete/<int:pk>', views.EmployeeDelete.as_view(), name = 'EmployeeDelete')
]