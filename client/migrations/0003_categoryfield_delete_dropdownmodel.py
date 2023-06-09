# Generated by Django 4.1.1 on 2022-09-20 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_dropdownmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selectfield', models.IntegerField(choices=[(True, 'yes'), (False, 'No')], default=1)),
                ('verified', models.BooleanField(default=True, verbose_name='Required?')),
            ],
        ),
        migrations.DeleteModel(
            name='DropdownModel',
        ),
    ]
