# Generated by Django 3.2.16 on 2023-07-06 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0045_alter_project_swabmaster_equip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(blank=True, max_length=128, null=True, unique=True, verbose_name='Project Name'),
        ),
    ]
