from django import forms 
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User 
from .models import medical_remainder,appointment_rest_data,medical_rest_data

class signupform(UserCreationForm):
    first_name=forms.CharField(max_length=50)
    email =forms.CharField(max_length=50)

    class meta:
        model=User 
        fields=('username')

class medical_remainder_form(forms.ModelForm):
    first_name=forms.CharField(max_length=100)
    email=forms.CharField(max_length=100)
    
class medical_rest_data_form(forms.ModelForm):
    email=forms.CharField(max_length=100)
    medicine_name=forms.CharField(max_length=100)
    does=forms.CharField(max_length=100)
    no_of_days=forms.CharField(max_length=100)
    remarks=forms.CharField(max_length=100)




