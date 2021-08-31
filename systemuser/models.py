from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class SystemUser(models.Model):
    admin_id = models.CharField(max_length=25)
    admin_status = models.CharField(max_length=25)


    




class Employee(models.Model):
    employee_type = models.CharField(max_length=255)
    employee_role = models.CharField(max_length=255)




class Voter(models.Model):

    citizen_registration_number = models.PositiveIntegerField()
    voter_name = models.CharField(max_length=100)
    voter_registratio_id = models.CharField(max_length=255)
    registration_date = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    voter_status = models.CharField(max_length=50)



    def changeVoterStatus(status):

         Voter.voter_status=status

    def __str__(self):
        return self.voter_name




 
