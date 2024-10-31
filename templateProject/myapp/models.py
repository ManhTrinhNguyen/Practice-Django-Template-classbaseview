from django.db import models

# Create your models here.
class Reservation(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  booking_time = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.first_name
  
class Employee(models.Model):
  name = models.CharField(max_length=100)   
  email = models.EmailField()   
  contact = models.CharField(max_length=15)   
  class Meta:   
    db_table = "Employee"
