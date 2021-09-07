from datetime import date
from django.core import validators
# from .validators import validate_age, validate_name, validate_name2
from systemuser import validators
from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.


class EvotingUser(models.Model):

    MALE='M'
    FEMALE='F'
    ACTIVE='A'
    INACTIVE='I'
    BANNED= 'B'

    GENDER_CHOICES = [ 
        (MALE,'Male'),(FEMALE,'Female'),
    ]

    SuperAdmin = 'SA'
    NEBEOFFICER = 'NO'
    VOTERREGISTRAR = 'VR'
    POLITICALPARTYREPRESENTATIVE = 'PRR'
    OBSERVER = 'O'
    VOTER = 'V'

    ROLE_CHOICES = [
        (SuperAdmin, 'SuperAdmin'), 
        (NEBEOFFICER, 'NEBE Officer'),
        (VOTERREGISTRAR, 'Voter Registrar'),
        (POLITICALPARTYREPRESENTATIVE, 'Political Party Representative'),
        (OBSERVER, 'Observer'),
        (VOTER, 'Voter')
    ]


    STATUS_CHOICES =[(ACTIVE,'Active'), (INACTIVE,'Inactive'), (BANNED,'Banned'),]

    first_name = models.CharField(max_length=100, validators=[validators.validate_name])
    middle_name = models.CharField(max_length=100, validators=[validators.validate_name])
    last_name = models.CharField(max_length=100, validators=[validators.validate_name])
    registration_date = models.DateField(default=date.today)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    role = models.CharField(choices=ROLE_CHOICES, default=VOTERREGISTRAR, max_length=50)
    date_of_birth = models.DateField(default=date.today) 
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=50)
    status = models.CharField(choices=STATUS_CHOICES ,max_length=15)
    

class SuperAdmin(EvotingUser):
    admin_id = models.CharField(max_length=25)
    admin_status = models.CharField(max_length=25)



    




class Employee(EvotingUser):
    employee_type = models.CharField(max_length=255)



class Voter(EvotingUser):

    VISION_IMPAIRMENT='V'
    DEAF_OR_HARD_OF_HEARING='D'
    PHYSICAL_DISABILITY='p'

    DISABILITY_CHOICES = [
        (VISION_IMPAIRMENT,'Vision Impairmnet'),(DEAF_OR_HARD_OF_HEARING,'Deaf or Hard of Hearing'),(PHYSICAL_DISABILITY, 'Physical Disability')]

    
    citizen_registration_number = models.PositiveIntegerField()
    voter_registratio_id = models.CharField(max_length=255) 
    registerd_at = models.CharField(max_length=255, default='Addis Ababa')
    woreda = models.IntegerField()
    sub_city = models.CharField(max_length=25)
    house_number = models.IntegerField()
    voted_at = models.CharField( max_length=255, default='will be foreign key to polling stations')
    voted_to = models.CharField(max_length=255, default='will be foreign key to candidates')
    voted_time = models.DateTimeField()
    at_polling_station = models.BooleanField(default=True)
    disabled = models.BooleanField(default= False)
    disability_type = models.CharField(choices=DISABILITY_CHOICES, max_length=50)
    duration_of_living_in_the_current_election_region = models.DurationField()


  

    def changeVoterStatus(status):

        #  Voter.status=status
        pass

    def __str__(self):
        # return self.first_name
        pass




 
