# Generated by Django 4.1.1 on 2022-12-08 06:50

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0104_alter_reactor_plant_alter_reactor_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reactor',
            name='unit',
            field=smart_selects.db_fields.GroupedForeignKey(group_field='plant', on_delete=django.db.models.deletion.CASCADE, related_name='reactorunit+', to='client.unit'),
        ),
    ]
