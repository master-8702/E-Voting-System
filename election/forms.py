from django import forms
from django.db.models import fields
from django.db.models.base import Model
from .models import Party, Election

class PartyForm(forms.ModelForm):

    class Meta:
        model = Party
        fields = '__all__'
        # exclude = ['voted_to']


class ElectionForm(forms.ModelForm):

    class Meta:
        model = Election
        fields = '__all__'

