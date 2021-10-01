from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from systemuser.models import Employee
from .models import ActionsToBeApproved, Candidates, Election, ElectionRegions, Observer, Party, PollingStation, Referendum, ReferendumOptions, Regions, Voter 

class RegionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Regions
        fields = '__all__'
        extra_kwargs = {
           
            
        }


class VoterSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Voter
        fields = '__all__' 
       

class CandidatesSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = Candidates
        fields = '__all__' 


class EmployeeSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        fields = '__all__' 


class PartySerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = Party
        fields = '__all__' 


class ElectionSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = Election
        fields = '__all__' 


class ReferendumSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = Referendum
        fields = '__all__' 


class ReferendumOptionsSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = ReferendumOptions
        fields = '__all__' 


class ObserverSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = Observer
        fields = '__all__' 


class ElectionRegionsSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = ElectionRegions
        fields = '__all__' 


class PollingStationSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = PollingStation
        fields = '__all__' 

