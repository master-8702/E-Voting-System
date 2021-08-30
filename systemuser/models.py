from django.db import models

# Create your models here.


class systemuser(models.Model):
    admin_id = models.CharField(max_length=25)
    admin_status = models.CharField(max_length=25)




class employee(models.Model):
    employee_type = models.CharField(max_length=255)
    employee_role = models.CharField(max_length=255)

