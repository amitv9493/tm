# Generated by Django 3.2.16 on 2023-06-06 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0047_auto_20230530_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bdd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.bdd')),
                ('calibratopn_stand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.calibration_stand')),
                ('swabmaster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.swabmaster')),
                ('ttd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.ttd')),
            ],
        ),
    ]