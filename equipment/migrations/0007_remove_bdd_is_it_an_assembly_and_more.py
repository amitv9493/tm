# Generated by Django 4.1.1 on 2022-10-19 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0006_remove_bdd_name_remove_calibration_stand_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bdd',
            name='is_it_an_assembly',
        ),
        migrations.RemoveField(
            model_name='calibration_stand',
            name='is_it_an_assembly',
        ),
        migrations.RemoveField(
            model_name='ttd',
            name='is_it_an_assembly',
        ),
    ]
