# Generated by Django 3.2.6 on 2021-09-29 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0005_actionstobeapproved'),
    ]

    operations = [
        migrations.AddField(
            model_name='actionstobeapproved',
            name='data',
            field=models.BinaryField(default=b'data'),
        ),
    ]
