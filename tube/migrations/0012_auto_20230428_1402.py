# Generated by Django 3.2.16 on 2023-04-28 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0011_warehouse_country'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Catalyst',
        ),
        migrations.DeleteModel(
            name='Loading',
        ),
    ]
