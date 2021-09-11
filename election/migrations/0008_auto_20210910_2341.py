# Generated by Django 3.2.6 on 2021-09-10 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0007_remove_party_candidate_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='referendum',
            old_name='referndum_name',
            new_name='referendum_name',
        ),
        migrations.AlterField(
            model_name='referendum',
            name='referendum_date',
            field=models.DurationField(default='P4DT1H15M20S'),
        ),
    ]
