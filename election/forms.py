from django import forms
from django.db.models import fields
from django.db.models.base import Model
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Party, Voter, Election, Referendum, ReferendumOptions, Candidates, ElectionRegions, PollingStation, Observer, Regions

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
        widgets = {
        'voter_password': forms.PasswordInput(),
        'voted_to': FilteredSelectMultiple("Voter", False, attrs={'rows':'2'})
        
    }
        # voted_to = forms.ModelMultipleChoiceField(Voter.objects.all(), widget=FilteredSelectMultiple("Voter", False, attrs={'rows':'10'}))

        class Media:
            extend = False
        css = {
            'all': [
                'admin/css/widgets.css'
            ]
        }
        js = (
            'js/django_global.js',
            'admin/js/jquery.init.js',
            'admin/js/core.js',
            'admin/js/prepopulate_init.js',
            'admin/js/prepopulate.js',
            'admin/js/SelectBox.js',
            'admin/js/SelectFilter2.js',
            'admin/js/admin/RelatedObjectLookups.js',
        )  

        # exclude = ['voted_to']
    #     voted_to = forms.MultipleChoiceField(
    #     required=False,
    #     widget=forms.CheckboxSelectMultiple,
        
    # )
        # 'voted_to': forms.SelectMultiple(),



class RegionsForm(forms.ModelForm):

    class Meta:
        model = Regions
        fields = '__all__'

class ElectionRegionsFrom(forms.ModelForm):

    class Meta:
        model = ElectionRegions
        fields = '__all__'



class PollingStationsForm(forms.ModelForm):

    class Meta:
        model = PollingStation
        fields = '__all__'
        

class ObserverForm(forms.ModelForm):

    class Meta:
        model = Observer
        fields = '__all__'

