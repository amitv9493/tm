# Generated by Django 3.2.16 on 2023-04-27 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0046_auto_20230314_0519'),
        ('client', '0125_auto_20230426_1324'),
        ('part', '0041_auto_20230426_1211'),
        ('project', '0039_alter_project_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='airhose_part',
            field=models.ManyToManyField(blank=True, default='', to='part.AirHose', verbose_name='Air Hose'),
        ),
        migrations.AlterField(
            model_name='project',
            name='bdd',
            field=models.ManyToManyField(blank=True, default='', related_name='bdd', to='equipment.BDD', verbose_name='BDD'),
        ),
        migrations.AlterField(
            model_name='project',
            name='calibration_orifice_part',
            field=models.ManyToManyField(blank=True, default='', to='part.Calibration_orifice', verbose_name='Calibration Orifice'),
        ),
        migrations.AlterField(
            model_name='project',
            name='calibration_stand',
            field=models.ManyToManyField(blank=True, related_name='calibration_stand', to='equipment.CALIBRATION_STAND', verbose_name='CALIBRATION STAND'),
        ),
        migrations.AlterField(
            model_name='project',
            name='device_part',
            field=models.ManyToManyField(blank=True, default='', to='part.DeviceHose', verbose_name='Device Hose'),
        ),
        migrations.AlterField(
            model_name='project',
            name='part',
            field=models.ManyToManyField(blank=True, default='', to='part.Part'),
        ),
        migrations.AlterField(
            model_name='project',
            name='pressure_sensor_part',
            field=models.ManyToManyField(blank=True, default='', to='part.Pressure_sensor', verbose_name='Pressure Sensor'),
        ),
        migrations.AlterField(
            model_name='project',
            name='reactor',
            field=models.ManyToManyField(blank=True, to='client.Reactor', verbose_name='Reactor Name'),
        ),
        migrations.AlterField(
            model_name='project',
            name='scope_of_work',
            field=models.ManyToManyField(blank=True, to='project.Scope_of_work', verbose_name='Scope Of Work'),
        ),
        migrations.AlterField(
            model_name='project',
            name='supply_orifice_part',
            field=models.ManyToManyField(blank=True, default='', to='part.Supply_orifice', verbose_name='Supply Orifice'),
        ),
        migrations.AlterField(
            model_name='project',
            name='swabmaster_part',
            field=models.ManyToManyField(blank=True, default='', to='part.SwabMasterTSR', verbose_name='Swab Master TSR'),
        ),
        migrations.AlterField(
            model_name='project',
            name='ttd',
            field=models.ManyToManyField(blank=True, default='', related_name='ttd', to='equipment.TTD', verbose_name='TTD'),
        ),
    ]
