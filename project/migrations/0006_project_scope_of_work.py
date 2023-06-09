# Generated by Django 4.1.1 on 2022-11-15 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_alter_project_equipment_delivery_client_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='scope_of_work',
            field=models.CharField(blank=True, choices=[('PD_TESTING', 'PD_TESTING'), ('BD', 'BD'), ('TC', 'TC'), ('JAC', 'JAC'), ('OLE', 'OLE'), ('FULL_TURN_KEY', 'FULL_TURN_KEY'), ('OTHER', 'OTHER')], default='PD_TESTING', max_length=128, verbose_name='Scope Of Work'),
        ),
    ]
