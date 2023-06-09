# Generated by Django 4.1.1 on 2022-12-12 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0025_alter_bdd_bdd_tube_seal_rack_and_more'),
        ('project', '0016_alter_project_contract_alter_project_scope_of_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scope_of_work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='equipment_info_remarks',
            field=models.CharField(default='', max_length=128, verbose_name='Equipment Info Remarks'),
        ),
        migrations.AddField(
            model_name='project',
            name='general_remarks',
            field=models.CharField(default='', max_length=128, verbose_name='General Remarks'),
        ),
        migrations.AlterField(
            model_name='project',
            name='calibration_stand',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='equipment.calibration_stand', verbose_name='CALIBRATION STAND'),
        ),
        migrations.AlterField(
            model_name='project',
            name='if_sub_client_name',
            field=models.CharField(blank=True, max_length=128, verbose_name='If Sub Contract Then Client Name'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_number',
            field=models.IntegerField(blank=True, default='1', verbose_name='Project Number'),
        ),
        migrations.AlterField(
            model_name='project',
            name='scope_of_work',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.scope_of_work', verbose_name='Scope Of Work'),
        ),
    ]
