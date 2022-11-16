from django import forms
from .models import patient
# write class here

class Register(forms.ModelForm):
    class Meta:
        model=patient
        fields='__all__'

