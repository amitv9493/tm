# Generated by Django 4.1.1 on 2022-09-22 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0028_remove_client_key_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='no_of_unit',
        ),
        migrations.RemoveField(
            model_name='client',
            name='reactor_per_each_unit',
        ),
    ]
