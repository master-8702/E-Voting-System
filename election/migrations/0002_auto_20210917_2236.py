# Generated by Django 3.2.6 on 2021-09-17 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='registerd_at',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='election.pollingstation'),
        ),
        migrations.AlterField(
            model_name='voter',
            name='voted_at',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='voted_place', to='election.pollingstation'),
        ),
    ]