# Generated by Django 3.2.16 on 2023-03-14 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0031_auto_20230303_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='bdd_part',
        ),
        migrations.RemoveField(
            model_name='project',
            name='ttd_part',
        ),
    ]
