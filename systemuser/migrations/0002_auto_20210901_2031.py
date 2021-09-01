# Generated by Django 3.2.6 on 2021-09-01 17:31

import django.core.validators
from django.db import migrations, models
import systemuser.validators


class Migration(migrations.Migration):

    dependencies = [
        ('systemuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='registerd_at',
            field=models.CharField(default='Addis Ababa', max_length=255),
        ),
        migrations.AddField(
            model_name='voter',
            name='voted_at',
            field=models.CharField(default='Addis Ababa', max_length=255),
        ),
        migrations.AlterField(
            model_name='voter',
            name='age',
            field=models.IntegerField(validators=[systemuser.validators.validate_age]),
        ),
        migrations.AlterField(
            model_name='voter',
            name='citizen_registration_number',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='voter',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=10),
        ),
        migrations.AlterField(
            model_name='voter',
            name='voter_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z]+$', 'Names contain non alphabetic character(s), only alphabets are allowed')]),
        ),
        migrations.AlterField(
            model_name='voter',
            name='voter_status',
            field=models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('B', 'Banned')], default='A', max_length=50),
        ),
    ]
