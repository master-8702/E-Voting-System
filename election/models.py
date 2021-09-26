from datetime import date
import election
from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, DateField
from systemuser import validators

# From here on we will define model classes that is found on the elelcton app(package)


#The following class is the model for our elelction Entity
MALE='Male'
FEMALE='Female'
GENDER_CHOICES = [ 
     (MALE,'Male'),(FEMALE,'Female'),
]
ACTIVE='Active'
INACTIVE='Inactive'
BANNED= 'Banned'

STATUS_CHOICES =[(ACTIVE,'Active'), (INACTIVE,'Inactive'), (BANNED,'Banned'),]

GENERAL = 'General'
REGIONAL = 'Regional'
LOCAL = 'Local'
FEDERAL = 'Federal'

ELECTION_TYPE_CHOICES = [
    (GENERAL, 'General'),
    (REGIONAL, 'Regional'),
    (LOCAL, 'Local'),
    (FEDERAL, 'Federal')
]

class Election(models.Model):

    election_name = models.CharField(max_length=255)
    election_registration_date = models.DateField(default=date.today)
    election_year = models.DateField()
    election_type = models.CharField(choices=ELECTION_TYPE_CHOICES ,max_length=255, default=GENERAL)
    election_date = models.DateField(default='2021-08-23') 
    election_result = models.CharField(max_length=255)
    election_regions = models.ForeignKey(to='ElectionRegions', on_delete=PROTECT)
    election_result = models.CharField(max_length=255, default='Election Result 1')
    elelction_status = models.CharField(STATUS_CHOICES ,max_length=25, default=ACTIVE)

#this method will return the elction name whenever we use the election object it self
    def __str__(self):
        return self.election_name

#this method will return the total number of candidates registered for the elelction term
    @property
    def candidate_number(self):
        return Candidates.objects.count()

#this method will return the total number of parties registered for the elelction term
    @property
    def party_number(self):
        return Party.objects.count()


#The following class is the model for our referendum Entity

class Referendum(models.Model):
    referendum_name = models.CharField(max_length=255)
    referendum_registration_date = models.DateField(default=date.today)
    referendum_date = models.DateField(default='2021-10-15')
    referendum_regions = models.ForeignKey(to='ElectionRegions', on_delete=PROTECT)
    referendum_result = models.CharField(max_length=25, default = 'Referendum Result 1')
    referendum_status = models.CharField(choices= STATUS_CHOICES ,max_length=255, default=ACTIVE)


    #here this method is going to tell us what options does a certain refendum has (using the foreign key 
    # in the other class)
    @property
    def referendum_options_list(self):
        b=""
        for a in self.referendumoptions_set.all():
            b += a.referendum_option_name +" | "
            print(b)
        return b 
       
   
    def __str__(self):
        return self.referendum_name


#The following class is the model for our referendumOptions Entity
class ReferendumOptions(models.Model):
    
    referendum_option_name = models.CharField(max_length=25)
    referendum = models.ForeignKey(to=Referendum, on_delete=PROTECT)
    number_of_votes = models.PositiveIntegerField(default=0)



    def __str__(self):
        return self.referendum_option_name


#The following class is the model for our Party Entity
class Party(models.Model):
    
    FEDERAL ='Federal'
    REGIONAL = 'Regional'
    PARTY_CHOICES=[
        (FEDERAL, 'Federal'),
        (REGIONAL, 'Regional')
    ]
    party_name = models.CharField(max_length=255)
    election = models.ForeignKey(to= Election, on_delete=PROTECT)
    party_registration_date = models.DateField(default=date.today)
    party_logo = models.ImageField(upload_to='files')
    party_type = models.CharField(choices=PARTY_CHOICES, max_length=255, default=FEDERAL)
    participation_regions = models.ManyToManyField(to='ElectionRegions')
    party_status = models.CharField(choices= STATUS_CHOICES ,max_length=25, default=ACTIVE)
    number_of_votes = models.PositiveBigIntegerField(default=0)
   # This method is gonna tell us the total number of candidates (which are related with Party by foreign key)
   # and it will act as a normal attribute propertiy of the class (since we add the @property class before it)
    @property
    def candidate_number(self):
        return self.candidates_set.count()

    @property
    def party_vote_counter(self):
        total_votes = 0
        for a in  self.candidates_set.all():
            total_votes += a.number_of_votes
        return total_votes

    # This method is gonna give us the party name whenever we access a given object of this class (if we 
    # don't specify which attribute to select(use) )
    def __str__(self):
        return self.party_name 

#The following class is the model for our Candidates Entity
class Candidates(models.Model):

    TEN_OR_BELOW = '10'
    DIPLOMA = 'DIPLOMA'
    BACHELOR_DEGREE ='BD'
    MASTERS_DEGREE = 'MD'
    PHD = 'Phd'
    PROFESSOR = 'Prf.'

    EDUCATION_LEVEL_CHOICES=[
       (TEN_OR_BELOW, '10 or Below'),
       (DIPLOMA, 'Diploma'),
       (BACHELOR_DEGREE, "Bachelor's Degree"),
       (MASTERS_DEGREE , "Master's Degree"),
       (PHD , 'Phd'),
       (PROFESSOR, 'Professor')
    ]
    PARTY ='Party'
    PERSONAL = 'Personal'

    CANDIDATE_TYPE_CHOICES=[
        (PARTY,'Party'),
        (PERSONAL, 'Personal')
    ]

    FOR_HOUSE_OF_PEOPLES_REPRESENTATIVES ="For House of Peoples' Representatives"
    FOR_REGIONAL_GOVERNMENT_COUNCIL = 'For Regional Government Council'

    PARTICIPATION_TYPE = [
        (FOR_HOUSE_OF_PEOPLES_REPRESENTATIVES, "For House of Peoples' Representatives"),
        (FOR_REGIONAL_GOVERNMENT_COUNCIL, 'For Regional Government Council')
    ]

    candidate_name = models.CharField(max_length=255)
    election = models.ForeignKey(to = Election, on_delete=PROTECT)
    candidate_DOB = models.DateField(default='1987-03-24')
    candidate_registration_date = models.DateField(default=date.today)
    Candidates_gender = models.CharField(choices=GENDER_CHOICES ,max_length=10)
    candidate_type = models.CharField(choices=CANDIDATE_TYPE_CHOICES,max_length=255, default=PARTY)
    education_level = models.CharField(choices=EDUCATION_LEVEL_CHOICES, max_length=25)
    participation_region = models.ManyToManyField(to='ElectionRegions')
    participates_for = models.CharField(choices=PARTICIPATION_TYPE, default= FOR_REGIONAL_GOVERNMENT_COUNCIL, max_length=50)
    candidate_photo = models.ImageField(upload_to='candidates_image/')
    candidate_status = models.CharField(choices= STATUS_CHOICES ,max_length=25, default=ACTIVE)
    party = models.ForeignKey(to=Party, on_delete=PROTECT, blank=True, null=True)
    number_of_votes = models.PositiveIntegerField(default=0)





    def __str__(self):
        return self.candidate_name


    @property
    def abc(self):
        print(self.electionregions_set.all())
        return  self.electionregions_set.all()  #self.candidates_set.all()
    
    @property
    def party_image(self):
        par = Party.objects.all().get(id=self.party_id)
        return par.part_logo
        

#The following class is the model for our Observer Entity
class Observer(models.Model):
    
    DOMESTIC = 'Domestic'; INTERNATIONAL = 'International'; MEDIA = 'Media'; POLITICAL_PARTY_AGENT = 'Political Party Agent'; CANDIDATE_AGENT = 'Candidate Agent'

    OBSERVER_TYPE_CHOICES = [
        (DOMESTIC, 'Domestic'), (INTERNATIONAL, 'International'), (MEDIA, 'Media'), (POLITICAL_PARTY_AGENT, 'Political Party Agent'), (CANDIDATE_AGENT, 'Candidate Agent')
    ]
    observer_name = models.CharField(max_length=50)
    election = models.ForeignKey(to= Election, on_delete=PROTECT, blank=True)
    referendum = models.ForeignKey(Referendum, on_delete=PROTECT, blank=True)
    observer_regisration_date = models.DateField(default=date.today)
    observer_organization = models.CharField(max_length=25)
    observer_type = models.CharField(choices=OBSERVER_TYPE_CHOICES ,max_length=255, default=POLITICAL_PARTY_AGENT)
    observer_status = models.CharField(choices= STATUS_CHOICES ,max_length=25, default=ACTIVE)



#The following class is the model for our Voter Entity
class Voter(models.Model):
    
    VISION_IMPAIRMENT='Vision Impairmnet'
    DEAF_OR_HARD_OF_HEARING='Deaf or Hard of Hearing'
    PHYSICAL_DISABILITY='Physical Disability'

    DISABILITY_CHOICES = [
        (VISION_IMPAIRMENT,'Vision Impairmnet'),(DEAF_OR_HARD_OF_HEARING,'Deaf or Hard of Hearing'),(PHYSICAL_DISABILITY, 'Physical Disability')]

    SIX_MONTHS = '6 Months'
    SEVEN_MONTHS_UPTO_AYEAR = '7 Months - 1 Year'
    TWO_YEARS = 'Two Years'
    TWO_UPTO_FIVE_YEARS = '2 - 5 Years'
    FIVE_UPTO_TEN_YEARS ='5 - 10 Years'
    TEN_UPTO_FIFTEEN_YEARS = '10 - 15 Years'
    FIFTEEN_UPTO_TWENTY_YEARS = '15 - 20 Years'
    MORE_THAN_TWENTY_YEARS = 'More Than 20 Years'

    LIVING_DURATION_CHOICES =[
        (SIX_MONTHS, '6 Months'),
        (SEVEN_MONTHS_UPTO_AYEAR, '7 Months - 1 Year'),
        (TWO_YEARS, 'Two Years'),
        (TWO_UPTO_FIVE_YEARS, '2 - 5 Years'),
        (FIVE_UPTO_TEN_YEARS, '5 - 10 Years'),
        (TEN_UPTO_FIFTEEN_YEARS, '10 - 15 Years'),
        (FIFTEEN_UPTO_TWENTY_YEARS, '15 - 20 Years'),
        (MORE_THAN_TWENTY_YEARS, 'More Than 20 Years')

    ]
    
    first_name = models.CharField(max_length=100, validators=[validators.validate_name()])
    middle_name = models.CharField(max_length=100, validators=[validators.validate_name()])
    last_name = models.CharField(max_length=100, validators=[validators.validate_name()]) 
    voter_password = models.CharField(max_length=25)
    election = models.ForeignKey(to=Election, on_delete=PROTECT, blank=True, null=True )
    referendum = models.ForeignKey(to=Referendum, on_delete=PROTECT, blank=True, null= True)
    registration_date = models.DateField(auto_now_add=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    citizen_registration_number = models.PositiveIntegerField()
    voter_registratio_id = models.CharField(max_length=255) 
    registerd_at = models.ForeignKey(to='PollingStation', on_delete=PROTECT)
    woreda = models.IntegerField()
    sub_city = models.CharField(max_length=25)
    house_number = models.IntegerField()
    voted_at = models.ForeignKey(to='PollingStation', related_name='voted_place', on_delete=PROTECT, blank=True, null=True)
    voted_to = models.ManyToManyField(to=Candidates, blank=True)  
    voted_time = models.DateTimeField(blank=True , null=True)
    at_polling_station = models.BooleanField(default=True, null=True)
    disabled = models.BooleanField(default= False)
    disability_type = models.CharField(choices=DISABILITY_CHOICES, max_length=50, default=None)
    voter_status = models.CharField(max_length=25,choices=STATUS_CHOICES, default=ACTIVE)
    duration_of_living_in_the_current_election_region = models.CharField(choices=LIVING_DURATION_CHOICES, max_length=50, default=SIX_MONTHS)

  

    def changeVoterStatus(status):

        #  Voter.status=status
        pass

    def __str__(self):
        return self.first_name
       
#The following class is the model for our Regions Entity
class Regions(models.Model):
    region_id = models.CharField(max_length=25)
    region_name = models.CharField(max_length=50)
    seats_for_HPR = models.PositiveIntegerField()  # HPR stands for House of Peoples' Representatives
    seats_for_RGC = models.PositiveIntegerField()  # RGC stands for regional government councils 
    region_status = models.CharField(choices=STATUS_CHOICES, default=ACTIVE, max_length=25)



    def __str__(self):

        return self.region_name

    @property
    def getHPRSeats(self):
        return self.seats_for_HPR
    @property
    def getRGCSeats(self):
        return self.seats_for_RGC

    @property
    def number_of_election_region(self):
        return self.electionregions_set.count()

#The following class is the model for our ElectionRegions Entity
class ElectionRegions(models.Model):
    election_region_id = models.CharField(max_length=25)
    election_region_name = models.CharField(max_length=25)
    regions = models.ForeignKey(to=Regions, on_delete= PROTECT)
    # location = models.CharField(max_length=255, default='will be changed to point datafield')
    seats_for_HPR = models.PositiveIntegerField()  # HPR stands for House of Peoples' Representatives
    seats_for_RGC = models.PositiveIntegerField()  # RGC stands for regional government councils 
    election_region_status = models.CharField(choices=STATUS_CHOICES, default=ACTIVE ,max_length=25)

# validator will be add for seats .. againest the total number of seats HPR=547, RGC=1991 (excluding tigray)
    @property
    def number_of_polling_stations(self):
        return self.pollingstation_set.count()

    @property
    def number_of_parties(self):
        return self.party_set.count()

    @property
    def number_of_candidates(self):
        return self.candidates_set.count()
    
    # @property
    def __str__(self):
        return self.election_region_name
    
    @property
    def getHPRSeats(self):
        return self.seats_for_HPR
    @property
    def getRGCSeats(self):
        return self.seats_for_RGC

#The following class is the model for our PollingStations Entity
class PollingStation(models.Model):
    polling_station_id = models.CharField(max_length=25)
    polling_station_name = models.CharField(max_length=50)
    election = models.ForeignKey(to= Election, on_delete=PROTECT)
    referendum = models.ForeignKey(to= Referendum, on_delete=PROTECT)
    found_in_region = models.ForeignKey(to=ElectionRegions, on_delete=PROTECT)
    polling_station_status = models.CharField(choices=STATUS_CHOICES ,max_length=25, default=ACTIVE)
    number_of_voters = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.polling_station_name

    @property
    def getregion(self):
        return self.found_in_region

#The following class is the model for our Analytics Entity
class Anlytics(models.Model):
    analytics_name = models.CharField(max_length=25)
    analytics_data = models.CharField(max_length=255)
    election = models.ForeignKey(to=Election, on_delete=PROTECT)
    referendum = models.ForeignKey(to=Referendum, on_delete=PROTECT)
