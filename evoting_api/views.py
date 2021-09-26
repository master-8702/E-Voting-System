from django.shortcuts import render

from rest_framework import viewsets
from .serializers import VoterSerializer, ReferendumOptionsSerializer
from election.models import Candidates,  ReferendumOptions


class VoterViewSet(viewsets.ModelViewSet):

    queryset = Candidates.objects.all().order_by('candidate_name')   
    serializer_class = VoterSerializer


class ReferendumOptionsViewSet(viewsets.ModelViewSet):

    queryset = ReferendumOptions.objects.all()  
    serializer_class = ReferendumOptionsSerializer