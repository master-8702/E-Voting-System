from django.core import validators
from django.utils.translation import activate
# from .validators import validate_age, validate_name, validate_name2
from systemuser import validators
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


trial = validators.RegexValidator(r'^[a-zA-Z]+$','Names can only be composed of alphabets')

class SystemUser(models.Model):
    admin_id = models.CharField(max_length=25)
    admin_status = models.CharField(max_length=25)


    




class Employee(models.Model):
    employee_type = models.CharField(max_length=255)
    employee_role = models.CharField(max_length=255)

MALE='M'
FEMALE='F'
ACTIVE='A'
INACTIVE='I'
BANNED= 'B'

GENDER_CHOICES = [
    (MALE,'Male'),(FEMALE,'Female'),]
VOTER_STATUS_CHOICES =[(ACTIVE,'Active'), (INACTIVE,'Inactive'), (BANNED,'Banned'),]

class Voter(models.Model):

    citizen_registration_number = models.PositiveIntegerField()
    voter_first_name = models.CharField(max_length=100, validators=[validators.validate_name()])
    voter_father_name = models.CharField(max_length=100, validators=[validators.validate_name()])
    voter_gfather_name = models.CharField(max_length=100, validators=[validators.validate_name()])
    voter_registratio_id = models.CharField(max_length=255) 
    registration_date = models.DateTimeField(auto_now_add=True)
    registerd_at = models.CharField(max_length=255, default='Addis Ababa')
    gender = models.CharField(choices=GENDER_CHOICES, default=MALE ,max_length=10)
    age = models.IntegerField(validators=[validators.validate_age]) 
    address = models.CharField(max_length=255)
    voted_at = models.CharField( max_length=255, default='Addis Ababa')
    voter_status = models.CharField(choices=VOTER_STATUS_CHOICES, default= ACTIVE, max_length=50)


  

    def changeVoterStatus(status):

         Voter.voter_status=status

    def __str__(self):
        return self.voter_first_name




 
