# Generated by Django 3.2.6 on 2021-09-21 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0005_alter_pollingstation_found_in_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='participation_regions',
            field=models.ManyToManyField(to='election.ElectionRegions'),
        ),
        migrations.AlterField(
            model_name='party',
            name='party_type',
            field=models.CharField(choices=[('Federal', 'Federal'), ('Regional', 'Regional')], max_length=255),
        ),
    ]