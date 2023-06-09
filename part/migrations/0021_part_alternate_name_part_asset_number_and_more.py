# Generated by Django 4.1.1 on 2023-01-18 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0005_remove_bdd_bdd_tube_seal_rack_and_more'),
        ('part', '0020_remove_part_pm_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='alternate_name',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='part',
            name='asset_number',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='part',
            name='is_this_part_of_set',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='part',
            name='it_is_an_assembly',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='part',
            name='location_for_storage',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='part',
            name='location_for_warehouse',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tube.warehouse'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='part',
            name='name_of_abbreviation',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='part',
            name='packaging',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='part',
            name='pm_status',
            field=models.CharField(choices=[('RED', 'RED'), ('BLUE', 'BLUE'), ('GREEN', 'GREEN')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='part',
            name='serial_number',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
