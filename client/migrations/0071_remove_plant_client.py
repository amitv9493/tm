# Generated by Django 4.1.1 on 2022-10-04 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0070_remove_client_plant_remove_plant_name_of_unit_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='client',
        ),
    ]
