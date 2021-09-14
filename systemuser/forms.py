from django import forms
from django.forms import fields
from .models import Employee, Voter
from django.contrib.auth.forms import UserCreationForm

class VoterForm(forms.ModelForm):

    class Meta:
        model = Voter
        fields = '__all__'
        # exclude = ['voted_to']



class EmployeeForm(UserCreationForm):

    class Meta:
        model = Employee
        fields = '__all__'




    