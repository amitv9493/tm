# Generated by Django 4.1.1 on 2022-10-04 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0062_remove_client_plant_remove_plant_name_of_unit_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='client',
        ),
        migrations.AddField(
            model_name='client',
            name='plant',
            field=models.ManyToManyField(related_name='client Plant+', to='client.plant'),
        ),
        migrations.AddField(
            model_name='plant',
            name='name_of_unit',
            field=models.ManyToManyField(related_name='plant Unit+', to='client.unit'),
        ),
    ]
