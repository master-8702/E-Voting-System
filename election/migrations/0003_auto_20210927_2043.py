# Generated by Django 3.2.6 on 2021-09-27 17:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0002_auto_20210927_1546'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='voter',
            options={},
        ),
        migrations.AlterModelManagers(
            name='voter',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='voter',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='voter',
            name='email',
        ),
        migrations.RemoveField(
            model_name='voter',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='voter',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='voter',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='voter',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='voter',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='voter',
            name='password',
        ),
        migrations.RemoveField(
            model_name='voter',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='voter',
            name='username',
        ),
        migrations.AddField(
            model_name='voter',
            name='voter_password',
            field=models.CharField(default=12345, max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='voter',
            name='first_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z]+$', 'Names contain non alphabetic character(s), only alphabets are allowed')]),
        ),
        migrations.AlterField(
            model_name='voter',
            name='last_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z]+$', 'Names contain non alphabetic character(s), only alphabets are allowed')]),
        ),
    ]