# Generated by Django 3.2.6 on 2021-09-14 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemuser', '0003_evotinguser_is_superadmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='evotinguser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]