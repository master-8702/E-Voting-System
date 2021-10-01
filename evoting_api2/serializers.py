from django.db.models import fields
from rest_framework import serializers
from election.models import Regions

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regions
        fields = '__all__'