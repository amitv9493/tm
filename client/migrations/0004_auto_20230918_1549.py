# Generated by Django 3.2.16 on 2023-09-18 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_alter_client_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reactor',
            name='select_tube_protude_bottom',
            field=models.CharField(blank=True, choices=[('INCH', 'INCH'), ('MM', 'MM')], max_length=128, null=True, verbose_name='Tube Protude Out Of Bottom Tube Sheet Unit'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='select_tube_protude_top',
            field=models.CharField(blank=True, choices=[('INCH', 'INCH'), ('MM', 'MM')], max_length=128, null=True, verbose_name='Tube Protude Top Unit'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='plant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='unitplant', to='client.plant'),
        ),
    ]
