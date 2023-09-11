# Generated by Django 3.2.16 on 2023-09-07 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0130_auto_20230705_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reactor',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reactorunit+', to='client.unit'),
        ),
    ]