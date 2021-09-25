from rest_framework import serializers
from election.models import Candidates, Voter


class VoterSerializer(serializers.ModelSerializer):

    
    class Meta:
            model = Candidates
            fields  = ['id', 'candidate_name', 'party', 'number_of_votes']
