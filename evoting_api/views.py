from django.shortcuts import render

from rest_framework import viewsets
from .serializers import VoterSerializer
from election.models import Candidates, Voter


class VoterViewSet(viewsets.ModelViewSet):

    queryset = Candidates.objects.all().order_by('candidate_name')   
    serializer_class = VoterSerializer