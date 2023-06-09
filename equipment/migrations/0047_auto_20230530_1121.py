# Generated by Django 3.2.16 on 2023-05-30 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0013_alter_warehouse_warehouse_contact'),
        ('equipment', '0046_auto_20230314_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bdd',
            name='location_for_warehouse',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bdd', to='tube.warehouse', verbose_name='Location For Warehouse'),
        ),
        migrations.AlterField(
            model_name='calibration_stand',
            name='location_for_warehouse',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='calibration_stand', to='tube.warehouse', verbose_name='Location For Warehouse'),
        ),
        migrations.AlterField(
            model_name='swabmaster',
            name='location_for_warehouse',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='swabmaster', to='tube.warehouse', verbose_name='Location For Warehouse'),
        ),
        migrations.AlterField(
            model_name='ttd',
            name='location_for_warehouse',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='ttd', to='tube.warehouse', verbose_name='Location For Warehouse'),
        ),
    ]
