from django import forms
from django.db.models import fields
from django.db.models.base import Model
from .models import Party, Voter, Election, Referendum, ReferendumOptions, Candidates, Regions, PollingStation, Observer

class PartyForm(forms.ModelForm):

    class Meta:
        model = Party
        fields = '__all__'
        # exclude = ['voted_to']


class ElectionForm(forms.ModelForm):

    class Meta:
        model = Election
        fields = '__all__'


class ReferendumForm(forms.ModelForm):

    class Meta:
        model = Referendum
        fields = '__all__'

class ReferendumOptionsForm(forms.ModelForm):

    class Meta:
        model = ReferendumOptions
        fields = '__all__'


class CandidatesForm(forms.ModelForm):

    class Meta:
        model = Candidates
        fields = '__all__'


class VoterForm(forms.ModelForm):
    
    class Meta:
        model = Voter
        fields = '__all__'
        # exclude = ['voted_to']


class RegionsFrom(forms.ModelForm):

    class Meta:
        model = Regions
        fields = '__all__'



class PollingStationsForm(forms.ModelForm):

    class Meta:
        model = PollingStation
        fields = '__all__'
        

class ObserverForm(forms.ModelForm):

    class Meta:
        model = Observer
        fields = '__all__'

