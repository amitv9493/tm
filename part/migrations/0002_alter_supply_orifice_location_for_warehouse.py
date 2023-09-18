# Generated by Django 3.2.16 on 2023-09-18 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0001_initial'),
        ('part', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supply_orifice',
            name='location_for_warehouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supply_orifice', to='tube.warehouse', verbose_name='Location For Warehouse'),
        ),
    ]
