# Generated by Django 4.1.1 on 2023-01-18 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0005_remove_bdd_bdd_tube_seal_rack_and_more'),
        ('part', '0015_alter_part_part_location_of_warehouse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='part_location_of_warehouse',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='tube.warehouse', verbose_name='Location For Warehouse'),
        ),
    ]
