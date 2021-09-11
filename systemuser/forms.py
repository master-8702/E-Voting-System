from django import forms
from django.forms import fields
from .models import Employee, Voter

class VoterForm(forms.ModelForm):

    class Meta:
        model = Voter
        fields = '__all__'
        # exclude = ['voted_to']



class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'




    