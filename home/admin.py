from django.contrib import admin
from home.models import Patient_Appointment,add_hospital_data,appointment_rest_data,medical_remainder

# Register your models here.
admin.site.register(Patient_Appointment)
admin.site.register(add_hospital_data)
admin.site.register(appointment_rest_data)
admin.site.register(medical_remainder)