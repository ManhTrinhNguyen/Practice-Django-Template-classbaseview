from django.test import TestCase
from datetime import datetime
from .models import Reservation, Employee

# Create your tests here.
class ReservationModelTest(TestCase):
  
  @classmethod
  def setUpTestData(cls):
    cls.reservation = Reservation.objects.create(
      first_name = 'John',
      last_name = 'McDonald'
    )

  def test_fields(self):
    self.assertIsInstance(self.reservation.first_name, str)
    self.assertIsInstance(self.reservation.last_name, str)


  def test_timestamps(self):
    self.assertIsInstance(self.reservation.booking_time, datetime)



class EmployeeTest(TestCase):
  @classmethod 
  def setUpTestData(cls):
    cls.employee = Employee.objects.create(
      name  = 'Tim',
      email = 'tim@gmail.com',
      contact = '123456'
    )

  def test_fields(self):
    self.assertIsInstance(self.employee.name, str)
    self.assertIsInstance(self.employee.email, str)
    self.assertIsInstance(self.employee.contact, str)