# Generated by Django 3.2.6 on 2021-09-10 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0008_auto_20210910_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='referendum',
            name='referendum_status',
            field=models.CharField(default='Active', max_length=255),
            preserve_default=False,
        ),
    ]
