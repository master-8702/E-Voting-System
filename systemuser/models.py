from datetime import date
# from guardian.mixins import GuardianUserMixin
from django.db.models.deletion import PROTECT
from election.models import Candidates, PollingStation
from django.core import validators
# from .validators import validate_age, validate_name, validate_name2
from systemuser import validators
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group, User
from datetime import date
from django.db.models.signals import post_save


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
        # we also can do set another attributes here when we create a certain user like:
        # user.is_observer = is_observer
        user.save(using = self._db)
        if user.role =='Observer':
            group = Group.objects.get(name='observer')
            user.groups.add(group)
        if user.role == 'nebe_officer':
            group = Group.objects.get(name='nebe_officer')
            user.groups.add(group)
        return user;


    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )

        user.is_nebe_officer = True
        user.is_observer = True
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.isEvoting_admin = True
        user.is_superuser = True

        user.save(using =self._db)
        return user




MALE='Male'
FEMALE='Female'
GENDER_CHOICES = [ 
     (MALE,'Male'),(FEMALE,'Female'),
]
ACTIVE='Active'
INACTIVE='Inactive'
BANNED= 'Banned'

STATUS_CHOICES =[(ACTIVE,'Active'), (INACTIVE,'Inactive'), (BANNED,'Banned'),]



class EvotingUser(AbstractBaseUser):
    
   
   

    

    SuperAdmin = 'SuperAdmin'
    NEBEOFFICER = 'NEBE Officer'
    VOTERREGISTRAR = 'Voter Registrar'
    POLITICALPARTYREPRESENTATIVE = 'PRR'
    OBSERVER = 'Observer'

    ROLE_CHOICES = [
        (SuperAdmin, 'SuperAdmin'), 
        (NEBEOFFICER, 'NEBE Officer'),
        (VOTERREGISTRAR, 'Voter Registrar'),
        (POLITICALPARTYREPRESENTATIVE, 'Political Party Representative'),
        (OBSERVER, 'Observer'),
    ]


    first_name = models.CharField(max_length=100, validators=[validators.validate_name()])
    middle_name = models.CharField(max_length=100, validators=[validators.validate_name()])
    last_name = models.CharField(max_length=100, validators=[validators.validate_name()]) 
    registration_date = models.DateField(auto_now_add=True)
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
    active = models.BooleanField(default=True)
    voter_registrar = models.BooleanField(default=False)
    nebe_officer = models.BooleanField(default=False)
    observer = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    Evoting_admin = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='files')

   

    USERNAME_FIELD ='username'  # if we want to add the email as the main username field
    # REQUIRED_FIELDS = ['username', 'first_name']  # to declare the required field on the form


    objects = EvotingUserManager()

    def __str__(self):
        return self.first_name + " "+ self.middle_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_lable):
        return True

    @property
    def is_active(self):
        return self.active

    @property
    def is_voter_registrar(self):
        return self.voter_registrar

    @property
    def is_nebe_officer(self):
        return self.nebe_officer

    @property
    def is_observer(self):
        return self.observer

    @property
    def is_Evoting_admin(self):
        return self.superadmin

    # this method will be called when user created signal is sent
    # def group_assigner(sender, instance, created, **kwargs):
    #     if created:
    #         user=instance
    #     if user.role =='Observer':
    #         group = Group.objects.get(name='observer')
    #         user.groups.add(group)
    #     if user.role == 'nebe_officer':
    #         group = Group.objects.get(name='nebe_officer')
    #         user.groups.add(group)
    
    # post_save.connect(group_assigner, sender=EvotingUser)
    





    

class SuperAdmin(EvotingUser):
    admin_id = models.CharField(max_length=25)
    admin_status = models.CharField(max_length=25)



    




class Employee(EvotingUser):
    employee_type = models.CharField(max_length=255)
    # employee_photo = models.ImageField(upload_to='files')

    @property 
    def get_image(self):
        return self.employee_photo.url







 
