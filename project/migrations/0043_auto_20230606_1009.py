# Generated by Django 3.2.16 on 2023-06-06 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0045_auto_20230530_1121'),
        ('project', '0042_alter_project_swabmaster_part'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='airhose_part',
            field=models.ManyToManyField(blank=True, default='', related_name='projects', to='part.AirHose', verbose_name='Air Hose'),
        ),
        migrations.AlterField(
            model_name='project',
            name='calibration_orifice_part',
            field=models.ManyToManyField(blank=True, default='', related_name='projects', to='part.Calibration_orifice', verbose_name='Calibration Orifice'),
        ),
        migrations.AlterField(
            model_name='project',
            name='device_part',
            field=models.ManyToManyField(blank=True, default='', related_name='projects', to='part.DeviceHose', verbose_name='Device Hose'),
        ),
        migrations.AlterField(
            model_name='project',
            name='pressure_sensor_part',
            field=models.ManyToManyField(blank=True, default='', related_name='projects', to='part.Pressure_sensor', verbose_name='Pressure Sensor'),
        ),
        migrations.AlterField(
            model_name='project',
            name='supply_orifice_part',
            field=models.ManyToManyField(blank=True, default='', related_name='projects', to='part.Supply_orifice', verbose_name='Supply Orifice'),
        ),
    ]