# Generated by Django 4.1.1 on 2022-09-21 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0013_delete_tubeidmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='TubeidModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=15)),
            ],
        ),
    ]
