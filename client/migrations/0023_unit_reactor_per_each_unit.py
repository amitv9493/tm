# Generated by Django 4.1.1 on 2022-09-21 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0022_plant_no_of_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='reactor_per_each_unit',
            field=models.ManyToManyField(to='client.reactor'),
        ),
    ]
