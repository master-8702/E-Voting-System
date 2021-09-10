from django.contrib import admin
from .models import Candidates, Election, Party

# Register your models here.
admin.site.register(Candidates)
admin.site.register(Party)
admin.site.register(Election)