from django.db import models

# Create your models here.
class patient(models.Model):
    patient_name=models.CharField(max_length=25)
    patient_phono=models.IntegerField(max_length=10)
    patient_age=models.IntegerField(max_length=2)
    patient_problm=models.TextField(max_length=100)
    patient_dob=models.DateField()


