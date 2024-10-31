from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Employee

# Create your views here.

# function View
def home(request):
  return render(request, 'index.html')

# Generic View
class HomeView(TemplateView):
  template_name = 'index.html'

def about(request):
  return render(request, 'about.html')

def menu(request):
  return render(request, 'menu.html')

# Generic Employee View
class EmployeeCreate(CreateView):
  model = Employee
  fields = '__all__'
  success_url = '/employees/list'

# Generic Employee List
class EmployeeList(ListView):
  model = Employee
  

# Generic Employee Detail 
class EmployeeDetail(DetailView):
  model = Employee 
  success_url = '/employees/success'

# Generic Employee Update 
class EmployeeUpdate(UpdateView):
  model = Employee
  fields = '__all__'
  success_url = '/employees/list' 

class EmployeeDelete(DeleteView):
  model = Employee
  success_url = '/employees/list'



