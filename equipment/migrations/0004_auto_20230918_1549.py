# Generated by Django 3.2.16 on 2023-09-18 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0003_alter_calibration_stand_calibration_orifice_set'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calibration_stand',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/cal_stand/'),
        ),
        migrations.AlterField(
            model_name='ttd',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/ttd/'),
        ),
    ]
