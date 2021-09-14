from datetime import date

from django.db.models.deletion import PROTECT
from election.models import Candidates
from django.core import validators
# from .validators import validate_age, validate_name, validate_name2
from systemuser import validators
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import date

# Create your models here.


class EvotingUserManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("You need an Email")
        if not username:
            raise ValueError("you need a username")

        user = self.model(
            email = self.normalize_email(email),
            username = username, 
        )
        user.set_password(password)
        user.save(using = self._db)
        return user;


    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True

        user.save(using =self._db)
        return user




class EvotingUser(AbstractBaseUser):
    
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

    first_name = models.CharField(max_length=100, validators=[validators.validate_name()])
    middle_name = models.CharField(max_length=100, validators=[validators.validate_name()])
    last_name = models.CharField(max_length=100, validators=[validators.validate_name()]) 
    registration_date = models.DateField(default=date.today)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    role = models.CharField(choices=ROLE_CHOICES, default=VOTERREGISTRAR, max_length=50)
    date_of_birth = models.DateField(default=date.today) 
    # username = models.CharField(max_length=15)
    # password = models.CharField(max_length=50)
    status = models.CharField(choices=STATUS_CHOICES ,max_length=15)
    # over riding the base user
    email = models.CharField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD ='username'  # if we want to add the email as the main username field
    # REQUIRED_FIELDS = ['username', 'first_name']  # to declare the required field on the form


    objects = EvotingUserManager()

    def __str__(self):
        return self.first_name + " "+ self.middle_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_lable):
        return True




    

class SuperAdmin(EvotingUser):
    admin_id = models.CharField(max_length=25)
    admin_status = models.CharField(max_length=25)



    




class Employee(EvotingUser):
    employee_type = models.CharField(max_length=255)
    employee_photo = models.ImageField(upload_to='files') 



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
    voted_to = models.ForeignKey(to=Candidates, on_delete=PROTECT)  
    voted_time = models.DateTimeField(auto_now_add=True)
    at_polling_station = models.BooleanField(default=True)
    disabled = models.BooleanField(default= False)
    disability_type = models.CharField(choices=DISABILITY_CHOICES, max_length=50)
    duration_of_living_in_the_current_election_region = models.DurationField(default='P4DT1H15M20S')


  

    def changeVoterStatus(status):

        #  Voter.status=status
        pass

    def __str__(self):
        return self.first_name
       



 
