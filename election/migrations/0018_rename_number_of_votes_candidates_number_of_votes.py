# Generated by Django 3.2.6 on 2021-09-22 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0017_alter_candidates_number_of_votes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidates',
            old_name='Number_of_votes',
            new_name='number_of_votes',
        ),
    ]