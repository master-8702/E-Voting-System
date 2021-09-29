from django.db.models import fields
from rest_framework import serializers
from .models import ActionsToBeApproved, Regions 

class RegionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Regions
        # fields = '__all__'
        exclude = ['id']

class ActionsToBeApprovedSerializer(serializers.ModelSerializer):

    entity = serializers.JSONField()
    class Meta:
        model  = ActionsToBeApproved
        fields = ['entity']

