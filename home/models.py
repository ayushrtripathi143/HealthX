from django.db import models

# Create your models here.
class Patient_Appointment(models.Model):
    name = models.CharField(max_length=30)
    mail = models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    dob=models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    city=models.CharField(max_length=30)
    dept=models.CharField(max_length=30)
    address=models.CharField(max_length=100)

class add_hospital_data(models.Model):
    name = models.CharField(max_length=30)
    mail = models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    capaity=models.CharField(max_length=10)
    oxygen=models.CharField(max_length=10,null=True)
    date=models.CharField(max_length=20)
    beds=models.CharField(max_length=10)
    city=models.CharField(max_length=30)
    dept=models.CharField(max_length=30)
    address=models.CharField(max_length=100)


class appointment_rest_data(models.Model):
    hospital=models.CharField(max_length=200)
    date=models.CharField(max_length=10,null=True)
    time=models.CharField(max_length=30,null=True)
    desc=models.CharField(max_length=2000,default="No",null=True)
    mail=models.CharField(max_length=20)
    dept=models.CharField(max_length=50)
    approved=models.CharField(max_length=20,default="",null=True)


class medical_remainder(models.Model):
    mail=models.CharField(max_length=50)
    Name=models.CharField(max_length=30)
    medicine_name=models.CharField(max_length=100,null=True)
    does=models.CharField(max_length=30,null=True)
    no_of_days=models.CharField(max_length=30,null=True)
    Remarks=models.CharField(max_length=200,null=True)

class medical_rest_data(models.Model):
    mail=models.CharField(max_length=50)
    Name=models.CharField(max_length=30)
    