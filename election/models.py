from django.db import models
from django.db.models.fields import CharField, DateField
from datetime import date

# Create your models here.


class Election(models.Model):

    election_name = models.CharField(max_length=255)
    election_registration_date = models.DateField(default=date.today)
    elelction_year = models.DateField()
    election_type = models.CharField(max_length=255, default='will be regional or federal')
    election_date = models.DurationField()
    election_result = models.CharField(max_length=255)
    political_parties = models.CharField(max_length=255)
    candidates = models.CharField(max_length=255)
    election_regions = models.CharField(max_length=255)
    polling_stations = models.CharField(max_length=255)
    observers = models.CharField(max_length=255)
    analytics = models.CharField(max_length=255)
    elelction_status = models.CharField(max_length=25)


class Referendum(models.Model):
    referndum_name = models.CharField(max_length=255)
    referendum_registration_date = models.DateField(default=date.today)
    referendum_date = models.DurationField()
    referendum_options = models.CharField(max_length=255, default='will be foreign key to referendumoptions')
    referendum_regions = models.CharField(max_length=25)
    referendum_stations = models.CharField(max_length=255, default='will be foreign key to referendum stations')
    referendum_observers = models.CharField(max_length=25, default='ggg')
    referendum_analytics = models.CharField(max_length=25)
    referendum_result = models.CharField(max_length=25)



class ReferendumOptions(models.Model):
    
    referendum_option_name = models.CharField(max_length=25)




    

class Party(models.Model):
    
    FEDERAL ='F'
    REGIONAL = 'R'
    PARTY_CHOICES=[
        (FEDERAL, 'Federal'),
        (REGIONAL, 'Regional')
    ]
    party_name = models.CharField(max_length=255)
    party_registration_date = models.DateField(default=date.today)
    part_logo = models.ImageField(upload_to='url here')
    party_type = models.CharField(choices=PARTY_CHOICES, max_length=255)
    participation_regions = CharField(max_length=255)
    candidates = models.CharField(max_length=255)
    party_status = models.CharField(max_length=25)


    
class Canidates(models.Model):

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
    candidate_DOB = models.DateField()
    candidate_registration_date = models.DateField(default=date.today)
    Candidates_gender = models.CharField(max_length=10)
    candidate_type = models.CharField(max_length=255, default='will be choices personal/party')
    education_level = CharField(choices=EDUCATION_LEVEL_CHOICES, max_length=25)
    participation_region = CharField(max_length=255)
    candidate_status = CharField(max_length=25)




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



class PollingStation(models.Model):
    polling_station_id = models.CharField(max_length=25)
    polling_station_name = models.CharField(max_length=25)
    found_in_region = models.CharField(max_length=255, default='foreign key to regions')
    list_of_candidates = models.CharField(max_length=255, default='foreign key to candidates')
    polling_station_status = models.CharField(max_length=25)


class Anlytics(models.Model):
    analytics_name = models.CharField(max_length=25)
    analytics_data = models.CharField(max_length=255)