from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, DateField
from datetime import date

# Create your models here.


class Election(models.Model):

    election_name = models.CharField(max_length=255)
    election_registration_date = models.DateField(default=date.today)
    election_year = models.DateField()
    election_type = models.CharField(max_length=255, default='will be regional or federal')
    election_date = models.DateField(default='2021-08-23') 
    election_result = models.CharField(max_length=255)
    political_parties = models.CharField(max_length=255)
    candidates = models.ForeignKey(to='Candidates', on_delete=PROTECT )
    election_regions = models.CharField(max_length=255)
    polling_stations = models.CharField(max_length=255)
    observers = models.CharField(max_length=255)
    analytics = models.CharField(max_length=255)
    elelction_status = models.CharField(max_length=25)


    def __str__(self):
        return self.election_name




class Referendum(models.Model):
    referendum_name = models.CharField(max_length=255)
    referendum_registration_date = models.DateField(default=date.today)
    referendum_date = models.DurationField(default='P4DT1H15M20S')
    # referendum_options = models.ForeignKey(to='ReferendumOptions', on_delete=PROTECT, default='Yihun')
    referendum_regions = models.CharField(max_length=25)
    referendum_stations = models.CharField(max_length=255, default='will be foreign key to referendum stations')
    referendum_observers = models.CharField(max_length=25, default='ggg')
    referendum_analytics = models.CharField(max_length=25)
    referendum_result = models.CharField(max_length=25)
    referendum_status = models.CharField(max_length=255)


    #here this method is going to tell us what options does a certain refendum has (using the foreign key 
    # in the other class)
    @property
    def referendum_options_list(self):
        b={}
        # for a in self.referendumoptions_set.all():
        #     b += a.referendum_option_name +", "
        #     print(b)
        # return b 
       
        for index, val in enumerate(self.referendumoptions_set.all()):
           
            b+=(index, val)
       
        # return self.referendumoptions_set.all()
        
    # @property
    # def referendum_options_list(self):
    #     return self.get_related_to(ReferendumOptions)
   
    def __str__(self):
        return self.referendum_name



class ReferendumOptions(models.Model):
    
    referendum_option_name = models.CharField(max_length=25)
    referendum = models.ForeignKey(to=Referendum, on_delete=PROTECT)



    def __str__(self):
        return self.referendum_option_name




    

class Party(models.Model):
    
    FEDERAL ='F'
    REGIONAL = 'R'
    PARTY_CHOICES=[
        (FEDERAL, 'Federal'),
        (REGIONAL, 'Regional')
    ]
    party_name = models.CharField(max_length=255)
    party_registration_date = models.DateField(default=date.today)
    part_logo = models.ImageField(upload_to='files')
    party_type = models.CharField(choices=PARTY_CHOICES, max_length=255)
    participation_regions = CharField(max_length=255)
    party_status = models.CharField(max_length=25)
    # candidate_list = models.ForeignKey(to='Candidates', on_delete=PROTECT, default=1)

   # This method is gonna tell us the total number of candidates (which are related with Party by foreign key)
   # and it will act as a normal attribute propertiy of the class (since we add the @property class before it)
    @property
    def candidate_number(self):
        return len(self.candidates_set.all())

    # This method is gonna give us the party name whenever we access a given object of this class (if we 
    # don't specify which attribute to select(use) )
    def __str__(self):
        return self.party_name 

    
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


    candidate_name = models.CharField(max_length=255)
    candidate_DOB = models.DateField(auto_now_add=True)
    candidate_registration_date = models.DateField(default=date.today)
    Candidates_gender = models.CharField(max_length=10)
    candidate_type = models.CharField(max_length=255, default='will be choices personal/party')
    education_level = CharField(choices=EDUCATION_LEVEL_CHOICES, max_length=25)
    participation_region = CharField(max_length=255)
    candidate_status = CharField(max_length=25)
    party = models.ForeignKey(to=Party, on_delete=PROTECT)





    def __str__(self):
        return self.candidate_name




class Observer(models.Model):
    Types_of_observers = models.CharField(max_length=25, default='DOMESTIC, INTERNATIONA, MEDIA, POLITICAL PARTY AGENT, CANDIDATE AGENT')
    observer_name = models.CharField(max_length=50)
    observer_regisration_date = models.DateField(default=date.today)
    observer_organization = models.CharField(max_length=25)
    observer_type = models.CharField(max_length=255, default='will be choices from types of choices')
    observer_status = models.CharField(max_length=25)




class Regions(models.Model):
    region_name = models.CharField(max_length=25)
    region_id = models.CharField(max_length=25)
    polling_stations =models.CharField(max_length=255, default='foreign key to polling stations')
    location = models.CharField(max_length=255, default='will be changed to point datafield')
    region_status = models.CharField(max_length=25)


    @property
    def number_of_polling_stations(self):
        return len(self.pollingstation_set.all())
    
    def __str__(self):
        return self.region_name


class PollingStation(models.Model):
    polling_station_id = models.CharField(max_length=25)
    polling_station_name = models.CharField(max_length=25)
    found_in_region = models.ForeignKey(to=Regions, on_delete=PROTECT)
    list_of_candidates = models.CharField(max_length=255, default='foreign key to candidates')
    polling_station_status = models.CharField(max_length=25)


    def __str__(self):
        return self.polling_station_name


class Anlytics(models.Model):
    analytics_name = models.CharField(max_length=25)
    analytics_data = models.CharField(max_length=255)