# Generated by Django 3.2.16 on 2023-09-18 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0001_initial'),
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bdd',
            name='BDD_tube_seal_rack',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bdd', to='part.bdd_tube_seal_rack', verbose_name='BDD Tube Seal Rack'),
        ),
    ]
