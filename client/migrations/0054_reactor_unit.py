# Generated by Django 4.1.1 on 2022-10-03 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0053_remove_plant_name_of_unit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reactor',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Unit Reactor+', to='client.client'),
        ),
    ]
