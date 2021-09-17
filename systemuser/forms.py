from django import forms
from django.forms import fields
from .models import Employee, EvotingUser
from django.contrib.auth.forms import UserCreationForm



class EmployeeForm(UserCreationForm):

    class Meta:
        model = EvotingUser
        fields = '__all__'




    