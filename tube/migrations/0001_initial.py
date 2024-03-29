# Generated by Django 3.2.16 on 2023-09-14 10:39

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warehouse_name', models.CharField(blank=True, max_length=128)),
                ('warehouse_location', models.CharField(blank=True, max_length=128)),
                ('warehouse_contact', models.CharField(blank=True, max_length=128)),
                ('warehouse_email', models.EmailField(blank=True, max_length=128)),
                ('warehouse_manager', models.CharField(blank=True, max_length=128)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True)),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
            ],
        ),
    ]
