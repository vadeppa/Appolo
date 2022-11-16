from django.contrib import admin
from .models import patient
# Register your models here.
@admin.register(patient)
class patientAdmin(admin.ModelAdmin):
    list_display = ['id','patient_name','patient_phono','patient_age','patient_problm','patient_dob']
