# Generated by Django 4.1.1 on 2022-09-20 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_alter_categoryfield_selectfield'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CategoryField',
        ),
    ]
