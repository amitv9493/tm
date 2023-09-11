# Generated by Django 3.2.16 on 2023-09-11 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0053_auto_20230907_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bdd',
            name='slug',
            field=models.SlugField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='calibration_stand',
            name='slug',
            field=models.SlugField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='swabmaster',
            name='serial_number',
            field=models.CharField(default=1, max_length=128, verbose_name='Serial Number'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='swabmaster',
            name='slug',
            field=models.SlugField(default=11, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ttd',
            name='slug',
            field=models.SlugField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
