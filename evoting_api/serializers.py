from rest_framework import serializers
from election.models import Candidates, ReferendumOptions


class VoterSerializer(serializers.ModelSerializer):

    
    class Meta:
            model = Candidates
            fields  = ['id', 'candidate_name', 'party', 'number_of_votes']


class ReferendumOptionsSerializer(serializers.ModelSerializer):
    
    
    class Meta:
            model = ReferendumOptions
            fields  = '__all__'
