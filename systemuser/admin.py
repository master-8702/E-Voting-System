from django.contrib.admin.sites import AdminSite
from systemuser.models import EvotingUser
from django.contrib import admin
from .models import EvotingUser

# Register your models here.

admin.site.register(EvotingUser)
