from django.contrib.admin.sites import AdminSite
from systemuser.models import SystemUser
from django.contrib import admin
from .models import SystemUser, Voter

# Register your models here.

admin.site.register(SystemUser)
admin.site.register(Voter)
