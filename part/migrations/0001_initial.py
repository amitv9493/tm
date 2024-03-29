# Generated by Django 3.2.16 on 2023-09-14 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tube', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TTD_tube_seal_rack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True)),
                ('size', models.CharField(blank=True, max_length=128)),
                ('qty_rack', models.CharField(blank=True, max_length=128)),
                ('tube_seal_rack', models.CharField(blank=True, max_length=128)),
                ('part_name', models.CharField(blank=True, max_length=128, null=True)),
                ('name_of_abbreviation', models.CharField(blank=True, max_length=128, verbose_name='Abbreviation')),
                ('asset_number', models.CharField(blank=True, max_length=128)),
                ('pm_status', models.CharField(blank=True, choices=[('RED', 'RED'), ('BLUE', 'BLUE'), ('GREEN', 'GREEN')], max_length=20, null=True)),
                ('location_for_storage', models.CharField(blank=True, max_length=128)),
                ('packaging', models.CharField(blank=True, max_length=128)),
                ('notes', models.TextField(blank=True, null=True)),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='media/images/general_parts')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Price')),
                ('weight_unit', models.CharField(blank=True, choices=[('KG', 'Kg'), ('LBS', 'Lbs')], max_length=50, null=True, verbose_name='Unit for Weight')),
                ('weight', models.PositiveIntegerField(blank=True, null=True, verbose_name='Weight')),
                ('length', models.PositiveIntegerField(blank=True, null=True)),
                ('breadth', models.PositiveIntegerField(blank=True, null=True)),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('dimension_unit', models.CharField(blank=True, choices=[('CM', 'Cm'), ('MM', 'Mm'), ('INCH', 'Inch')], max_length=50, null=True, verbose_name='Unit for Dimensions')),
                ('location_for_warehouse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ttd_rack', to='tube.warehouse', verbose_name='Location For Warehouse')),
            ],
            options={
                'verbose_name': 'TDD Tube Seal Rack',
            },
        ),
        migrations.CreateModel(
            name='SwabMasterTSR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=128, unique=True)),
                ('size', models.CharField(blank=True, max_length=128)),
                ('qty_rack', models.CharField(blank=True, max_length=128)),
                ('tube_seal_rack', models.CharField(blank=True, max_length=128)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True)),
                ('part_name', models.CharField(blank=True, max_length=128, null=True)),
                ('name_of_abbreviation', models.CharField(blank=True, max_length=128, verbose_name='Abbreviation')),
                ('asset_number', models.CharField(blank=True, max_length=128)),
                ('pm_status', models.CharField(blank=True, choices=[('RED', 'RED'), ('BLUE', 'BLUE'), ('GREEN', 'GREEN')], max_length=20, null=True)),
                ('location_for_storage', models.CharField(blank=True, max_length=128)),
                ('packaging', models.CharField(blank=True, max_length=128)),
                ('notes', models.TextField(blank=True, null=True)),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='media/images/general_parts')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Price')),
                ('length', models.PositiveIntegerField(blank=True, null=True)),
                ('breadth', models.PositiveIntegerField(blank=True, null=True)),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('dimension_unit', models.CharField(blank=True, choices=[('CM', 'Cm'), ('MM', 'Mm'), ('INCH', 'Inch')], max_length=50, null=True, verbose_name='Unit for Dimensions')),
                ('weight_unit', models.CharField(blank=True, choices=[('KG', 'Kg'), ('LBS', 'Lbs')], max_length=50, null=True, verbose_name='Unit for Weight')),
                ('weight', models.PositiveIntegerField(blank=True, null=True, verbose_name='Weight')),
                ('location_for_warehouse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='swabmasterTSR', to='tube.warehouse', verbose_name='Location For Warehouse')),
            ],
            options={
                'verbose_name': 'SwabMaster Tube Seal Rack',
            },
        ),
        migrations.CreateModel(
            name='Supply_orifice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=128, unique=True)),
                ('size', models.CharField(blank=True, max_length=128)),
                ('total_sets', models.CharField(blank=True, max_length=128)),
                ('orifice_in_each_set', models.CharField(blank=True, max_length=128)),
                ('storage_case', models.CharField(blank=True, max_length=128)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True)),
                ('part_name', models.CharField(blank=True, max_length=128, null=True)),
                ('name_of_abbreviation', models.CharField(blank=True, max_length=128, verbose_name='Abbreviation')),
                ('asset_number', models.CharField(blank=True, max_length=128)),
                ('pm_status', models.CharField(blank=True, choices=[('RED', 'RED'), ('BLUE', 'BLUE'), ('GREEN', 'GREEN')], max_length=20, null=True)),
                ('location_for_storage', models.CharField(blank=True, max_length=128)),
                ('packaging', models.CharField(blank=True, max_length=128)),
                ('notes', models.TextField(blank=True, null=True)),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='media/images/general_parts')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Price')),
                ('weight_unit', models.CharField(blank=True, choices=[('KG', 'Kg'), ('LBS', 'Lbs')], max_length=50, null=True, verbose_name='Unit for Weight')),
                ('weight', models.PositiveIntegerField(blank=True, null=True, verbose_name='Weight')),
                ('length', models.PositiveIntegerField(blank=True, null=True)),
                ('breadth', models.PositiveIntegerField(blank=True, null=True)),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('dimension_unit', models.CharField(blank=True, choices=[('CM', 'Cm'), ('MM', 'Mm'), ('INCH', 'Inch')], max_length=50, null=True, verbose_name='Unit for Dimensions')),
                ('location_for_warehouse', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supply_orifice', to='tube.warehouse', verbose_name='Location For Warehouse')),
            ],
            options={
                'verbose_name': 'Supply Orifice',
            },
        ),
        migrations.CreateModel(
            name='Pressure_sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=128, unique=True)),
                ('range', models.CharField(blank=True, max_length=128)),
                ('quantity', models.CharField(blank=True, max_length=128)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True)),
                ('part_name', models.CharField(blank=True, max_length=128, null=True)),
                ('name_of_abbreviation', models.CharField(blank=True, max_length=128, verbose_name='Abbreviation')),
                ('asset_number', models.CharField(blank=True, max_length=128)),
                ('pm_status', models.CharField(blank=True, choices=[('RED', 'RED'), ('BLUE', 'BLUE'), ('GREEN', 'GREEN')], max_length=20, null=True)),
                ('location_for_storage', models.CharField(blank=True, max_length=128)),
                ('packaging', models.CharField(blank=True, max_length=128)),
                ('notes', models.TextField(blank=True, null=True)),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='media/images/general_parts')),
                ('weight_unit', models.CharField(blank=True, choices=[('KG', 'Kg'), ('LBS', 'Lbs')], max_length=50, null=True, verbose_name='Unit for Weight')),
                ('weight', models.PositiveIntegerField(blank=True, null=True, verbose_name='Weight')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Price')),
                ('length', models.PositiveIntegerField(blank=True, null=True)),
                ('breadth', models.PositiveIntegerField(blank=True, null=True)),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('dimension_unit', models.CharField(blank=True, choices=[('CM', 'Cm'), ('MM', 'Mm'), ('INCH', 'Inch')], max_length=50, null=True, verbose_name='Unit for Dimensions')),
                ('location_for_warehouse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pressure_sensor', to='tube.warehouse', verbose_name='Location For Warehouse')),
            ],
            options={
                'verbose_name': 'Pressure Sensor',
            },
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_name', models.CharField(blank=True, max_length=128)),
                ('name_of_abbreviation', models.CharField(blank=True, max_length=128, verbose_name='Abbreviation')),
                ('serial_number', models.CharField(max_length=128, unique=True)),
                ('asset_number', models.CharField(blank=True, max_length=128)),
                ('pm_status', models.CharField(blank=True, choices=[('RED', 'RED'), ('BLUE', 'BLUE'), ('GREEN', 'GREEN')], max_length=20, null=True)),
                ('location_for_storage', models.CharField(blank=True, max_length=128)),
                ('packaging', models.CharField(blank=True, max_length=128)),
                ('notes', models.TextField(blank=True, null=True)),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='media/images/general_parts')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Price')),
                ('weight_unit', models.CharField(blank=True, choices=[('KG', 'Kg'), ('LBS', 'Lbs')], max_length=50, null=True, verbose_name='Unit for Weight')),
                ('weight', models.PositiveIntegerField(blank=True, null=True, verbose_name='Weight')),
                ('length', models.PositiveIntegerField(blank=True, null=True)),
                ('breadth', models.PositiveIntegerField(blank=True, null=True)),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('dimension_unit', models.CharField(blank=True, choices=[('CM', 'Cm'), ('MM', 'Mm'), ('INCH', 'Inch')], max_length=50, null=True, verbose_name='Unit for Dimensions')),
                ('slug', models.SlugField(blank=True, max_length=500, null=True)),
                ('location_for_warehouse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='part', to='tube.warehouse')),
            ],
            options={
                'verbose_name': 'All General Part',
            },
        ),
        migrations.CreateModel(
            name='DeviceHose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=999, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True)),
                ('colour_code', models.CharField(blank=True, max_length=50, null=True)),
                ('part_name', models.CharField(blank=True, max_length=128, null=True)),
                ('name_of_abbreviation', models.CharField(blank=True, max_length=128, verbose_name='Abbreviation')),
                ('asset_number', models.CharField(blank=True, max_length=128)),
                ('pm_status', models.CharField(blank=True, choices=[('RED', 'RED'), ('BLUE', 'BLUE'), ('GREEN', 'GREEN')], max_length=20, null=True)),
                ('location_for_storage', models.CharField(blank=True, max_length=128)),
                ('packaging', models.CharField(blank=True, max_length=128)),
                ('notes', models.TextField(blank=True, null=True)),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='media/images/general_parts')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Price')),
                ('length', models.PositiveIntegerField(blank=True, null=True)),
                ('breadth', models.PositiveIntegerField(blank=True, null=True)),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('dimension_unit', models.CharField(blank=True, choices=[('CM', 'Cm'), ('MM', 'Mm'), ('INCH', 'Inch')], max_length=50, null=True, verbose_name='Unit for Dimensions')),
                ('weight_unit', models.CharField(blank=True, choices=[('KG', 'Kg'), ('LBS', 'Lbs')], max_length=50, null=True, verbose_name='Unit for Weight')),
                ('weight', models.PositiveIntegerField(blank=True, null=True, verbose_name='Weight')),
                ('warehouse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='devicehose', to='tube.warehouse')),
            ],
            options={
                'verbose_name': 'Device Hose',
            },
        ),
        migrations.CreateModel(
            name='Calibration_orifice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=128, unique=True)),
                ('size', models.CharField(blank=True, max_length=128)),
                ('total_sets', models.CharField(blank=True, max_length=128)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True)),
                ('in_sets', models.CharField(blank=True, max_length=128)),
                ('part_name', models.CharField(blank=True, max_length=128, null=True)),
                ('name_of_abbreviation', models.CharField(blank=True, max_length=128, verbose_name='Abbreviation')),
                ('asset_number', models.CharField(blank=True, max_length=128)),
                ('pm_status', models.CharField(blank=True, choices=[('RED', 'RED'), ('BLUE', 'BLUE'), ('GREEN', 'GREEN')], max_length=20, null=True)),
                ('location_for_storage', models.CharField(blank=True, max_length=128)),
                ('packaging', models.CharField(blank=True, max_length=128)),
                ('notes', models.TextField(blank=True, null=True)),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='media/images/general_parts')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Price')),
                ('length', models.PositiveIntegerField(blank=True, null=True)),
                ('breadth', models.PositiveIntegerField(blank=True, null=True)),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('dimension_unit', models.CharField(blank=True, choices=[('CM', 'Cm'), ('MM', 'Mm'), ('INCH', 'Inch')], max_length=50, null=True, verbose_name='Unit for Dimensions')),
                ('weight_unit', models.CharField(blank=True, choices=[('KG', 'Kg'), ('LBS', 'Lbs')], max_length=50, null=True, verbose_name='Unit for Weight')),
                ('weight', models.PositiveIntegerField(blank=True, null=True, verbose_name='Weight')),
                ('location_for_warehouse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='calibration_orifice', to='tube.warehouse', verbose_name='Location For Warehouse')),
            ],
            options={
                'verbose_name': 'Calibration Orifice',
            },
        ),
        migrations.CreateModel(
            name='BDD_tube_seal_rack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=128, unique=True)),
                ('size', models.CharField(blank=True, max_length=128)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True)),
                ('number_of_tubes', models.PositiveIntegerField(blank=True, null=True)),
                ('part_name', models.CharField(blank=True, max_length=128, null=True)),
                ('name_of_abbreviation', models.CharField(blank=True, max_length=128, verbose_name='Abbreviation')),
                ('asset_number', models.CharField(blank=True, max_length=128)),
                ('pm_status', models.CharField(blank=True, choices=[('RED', 'RED'), ('BLUE', 'BLUE'), ('GREEN', 'GREEN')], max_length=20, null=True)),
                ('location_for_storage', models.CharField(blank=True, max_length=128)),
                ('packaging', models.CharField(blank=True, max_length=128)),
                ('notes', models.TextField(blank=True, null=True)),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='media/images/general_parts')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Price')),
                ('length', models.PositiveIntegerField(blank=True, null=True)),
                ('breadth', models.PositiveIntegerField(blank=True, null=True)),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('dimension_unit', models.CharField(blank=True, choices=[('CM', 'Cm'), ('MM', 'Mm'), ('INCH', 'Inch')], max_length=50, null=True, verbose_name='Unit for Dimensions')),
                ('weight_unit', models.CharField(blank=True, choices=[('KG', 'Kg'), ('LBS', 'Lbs')], max_length=50, null=True, verbose_name='Unit for Weight')),
                ('weight', models.PositiveIntegerField(blank=True, null=True, verbose_name='Weight')),
                ('location_for_warehouse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bdd_rack', to='tube.warehouse', verbose_name='Location For Warehouse')),
            ],
            options={
                'verbose_name': 'BDD Tube Seal Rack',
            },
        ),
        migrations.CreateModel(
            name='AirHose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=999, unique=True)),
                ('colour_code', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True)),
                ('part_name', models.CharField(blank=True, max_length=128, null=True)),
                ('name_of_abbreviation', models.CharField(blank=True, max_length=128, verbose_name='Abbreviation')),
                ('asset_number', models.CharField(blank=True, max_length=128)),
                ('pm_status', models.CharField(blank=True, choices=[('RED', 'RED'), ('BLUE', 'BLUE'), ('GREEN', 'GREEN')], max_length=20, null=True)),
                ('location_for_storage', models.CharField(blank=True, max_length=128)),
                ('packaging', models.CharField(blank=True, max_length=128)),
                ('notes', models.TextField(blank=True, null=True)),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='media/images/general_parts')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Price')),
                ('length', models.PositiveIntegerField(blank=True, null=True)),
                ('breadth', models.PositiveIntegerField(blank=True, null=True)),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('dimension_unit', models.CharField(blank=True, choices=[('CM', 'Cm'), ('MM', 'Mm'), ('INCH', 'Inch')], max_length=50, null=True, verbose_name='Unit for Dimensions')),
                ('weight_unit', models.CharField(blank=True, choices=[('KG', 'Kg'), ('LBS', 'Lbs')], max_length=50, null=True, verbose_name='Unit for Weight')),
                ('weight', models.PositiveIntegerField(blank=True, null=True, verbose_name='Weight')),
                ('warehouse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='airhose', to='tube.warehouse')),
            ],
            options={
                'verbose_name': 'Air Hose',
            },
        ),
    ]
