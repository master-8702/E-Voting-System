from django.contrib import admin
from .models import Candidates, Election, ElectionRegions, Observer, Party, PollingStation, Referendum, ReferendumOptions, Regions, Voter

# Register your models here.
admin.site.register(Candidates)
admin.site.register(Party)
admin.site.register(Election)
admin.site.register(ElectionRegions)
admin.site.register(Regions)
admin.site.register(Voter)
admin.site.register(PollingStation)
admin.site.register(Observer)
admin.site.register(Referendum)
admin.site.register(ReferendumOptions)