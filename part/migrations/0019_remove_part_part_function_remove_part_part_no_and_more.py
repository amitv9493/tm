# Generated by Django 4.1.1 on 2023-01-18 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0018_remove_part_pm_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='part_function',
        ),
        migrations.RemoveField(
            model_name='part',
            name='part_no',
        ),
        migrations.AddField(
            model_name='part',
            name='PM_STATUS',
            field=models.CharField(blank=True, choices=[('Red', 'Red'), ('Blue', 'Blue'), ('Green', 'Green')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='part',
            name='is_this_part_of_set',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=128, null=True, verbose_name='Is This Part Of Set?'),
        ),
        migrations.AddField(
            model_name='part',
            name='it_is_an_assembly',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=128, null=True, verbose_name='It is an assembly?'),
        ),
        migrations.AddField(
            model_name='part',
            name='packaging',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='part',
            name='part_alternate_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='part',
            name='part_asset_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Asset Number'),
        ),
        migrations.AddField(
            model_name='part',
            name='part_location_of_storage',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Location For Storage'),
        ),
        migrations.AddField(
            model_name='part',
            name='part_serial_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Serial Number'),
        ),
        migrations.AlterField(
            model_name='part',
            name='part_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
