# Generated by Django 3.2.16 on 2023-02-09 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0038_alter_bdd_bdd_tube_seal_rack'),
    ]

    operations = [
        migrations.AddField(
            model_name='ttd',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='calibration_stand',
            name='pm_status',
            field=models.CharField(blank=True, choices=[('RED', 'RED'), ('BLUE', 'BLUE'), ('GREEN', 'GREEN')], max_length=20, null=True, verbose_name='PM Status'),
        ),
    ]
