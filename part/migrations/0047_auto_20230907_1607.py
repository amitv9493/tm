# Generated by Django 3.2.16 on 2023-09-07 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0046_auto_20230705_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airhose',
            name='serial_number',
            field=models.CharField(max_length=999, unique=True),
        ),
        migrations.AlterField(
            model_name='bdd_tube_seal_rack',
            name='serial_number',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='calibration_orifice',
            name='serial_number',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='devicehose',
            name='serial_number',
            field=models.CharField(max_length=999, unique=True),
        ),
        migrations.AlterField(
            model_name='part',
            name='serial_number',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='pressure_sensor',
            name='serial_number',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='supply_orifice',
            name='serial_number',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='swabmastertsr',
            name='serial_number',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='ttd_tube_seal_rack',
            name='serial_number',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
